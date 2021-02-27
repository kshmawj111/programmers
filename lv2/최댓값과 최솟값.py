# https://programmers.co.kr/learn/courses/30/lessons/12939?language=python3


def solution(s):
    answer = []
    i = 0
    while i < len(s):
        parsed = ''
        while i < len(s) and s[i] != ' ':
            parsed += s[i]
            i += 1

        answer.append(int(parsed))
        i += 1

    answer.sort()

    answer = ''.join([str(answer[0]), ' ', str(answer[-1])])
    return answer


if __name__ == '__main__':
    s = '1 2 3 4 5 -1 9 -10'
    print(solution(s))

    s = '-1 -1'
    print(solution(s))
