# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3


import math
from itertools import permutations


def is_prime(number):
    result = True

    if number <= 1:
        return False

    if number == 2:
        return True

    for i in range(2, int(math.sqrt(number)) + 1):

        if number % i == 0:
            result = False

    return result


def solution(numbers: str):
    result = []
    for length in range(1, len(numbers)+1):
        for comb in permutations(numbers, length):
            number = int(''.join(comb))

            if is_prime(number):
                result.append(number)

    result = set(result)
    print(result)
    return len(result)


if __name__ == '__main__':
    n = '17'
    solution(n)

    n= '011'
    solution(n)