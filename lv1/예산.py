# https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3

from itertools import accumulate


def solution(d, budget):
    d = sorted(d)
    d = list(accumulate(d))

    answer = len(d)
    for i, v in zip(range(len(d)), d):
        if v > budget:
            answer = i
            break

    return answer


if __name__ == '__main__':
    d = [1,3,2,5,4]
    b = 9

    print(solution(d, b))

    d = [2,2,3,3]
    b = 10

    print(solution(d, b))