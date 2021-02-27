# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3
from copy import deepcopy


def is_changeable(w1, w2):
    diff_count = 0

    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff_count += 1

        if diff_count > 1:
            return False

    return True


def solution(begin, target, words):
    answer = 100
    brach_list = []
    changed_list = [begin]
    history = []
    words.sort(reverse=False)

    if target not in words:
        return 0

    while changed_list or brach_list:
        prev = changed_list.pop()
        brach_list.append(deepcopy(changed_list))

        history.append(prev)
        temp = []

        for w in words:
            if is_changeable(prev, w) and w not in history:
                if w == target:
                    history.append(w)

                    if answer > len(history):
                        answer = len(history) - 1
                        
                    last_branch = None

                    while not last_branch and brach_list:
                        last_branch = brach_list.pop()

                    history = history[:len(brach_list)]
                    temp = last_branch

                    break

                temp.append(w)

        changed_list = temp

    return answer


if __name__ == '__main__':
    b, t, w = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(b, t, w))