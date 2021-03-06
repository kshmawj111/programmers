# https://programmers.co.kr/learn/courses/30/lessons/12936?language=python3
import math
from itertools import permutations


def calculate_first(k, num_list:list):
    _fact = math.factorial(len(num_list) - 1)

    if k % _fact == 0:
        idx = k // _fact - 1

    else:
        idx = k // _fact

    result = num_list.pop(idx)
    return result


def solution(n, k):
    answer = []
    possible_nums = [x for x in range(1, n+1)]

    while possible_nums:
        k = k % math.factorial(len(possible_nums))
        found_num = calculate_first(k, possible_nums)
        answer.append(found_num)

    return answer


if __name__ == '__main__':
    n, k = 4, 16
    print(list(permutations([i for i in range(1, n+1)]))[k-1])

    print(solution(n, k))
