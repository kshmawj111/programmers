# https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3
from itertools import combinations
from functools import reduce
from math import sqrt


def is_prime(n):
    if n != 1:
        for x in range(2, int(sqrt(n)+1)):
            if n % x == 0:
                return 0

        return 1

    else:
        return 0


def solution(nums):
    return reduce(lambda x, y: x+is_prime(y), map(lambda x: sum(x), combinations(nums, 3)), 0)


if __name__ == '__main__':
    n = [1,2,3,4]
    print(solution(n))
