# https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

import functools
from itertools import combinations


def set_diff(arr):
    result = [arr[0]]

    def return_diff(reference, mutable_element):
        if reference != mutable_element:
            result.append(mutable_element)
            return mutable_element

        else:
            return reference

    functools.reduce(return_diff, arr)
    return result


def solution(numbers: list):
    combs = combinations(numbers, 2)
    result = functools.reduce(
        lambda x, y:
        [functools.reduce(lambda c1, c2: c1+c2, x)] if isinstance(x, tuple)

        else x + [functools.reduce(lambda c1, c2: c1+c2, y)] if x[-1] != functools.reduce(lambda c1, c2: c1+c2, y)
            else x,

        combs)

    result = sorted(result)
    result = set_diff(result)
    return result


if __name__ == '__main__':
    print(solution([2,1,3,4,1]))