# https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3


def is_in_prev(words, word):
    for x in words:
        if x == word:
            return True

    return False


def solution(n, words):
    answer = [0, 0]
    record = {0: 1}
    prev_word = words[0]
    for w_i in range(1, len(words)):

        if w_i % n in record.keys():
            record[w_i % n] += 1

        else:
            record[w_i % n] = 1

        if words[w_i][0] != prev_word[-1] or is_in_prev(words[:w_i], words[w_i]):
            answer = [(w_i % n) +1, record[w_i % n]]
            break

        prev_word = words[w_i]

    return answer


if __name__ == '__main__':
    n = 3
    w = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
    print(solution(n, w))