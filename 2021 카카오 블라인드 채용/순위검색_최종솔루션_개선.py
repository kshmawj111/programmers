# https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3
import re


def parse_info(string: str):
    parsed = re.split(' and | ', string)
    score = int(parsed[-1])
    key = ''.join(parsed[:-1])
    return key, score


def mask_string(key_string: str):
    keys = re.split(' ', key_string)
    score = int(keys[-1])
    result = []
    l = [keys[0], '-']
    p = [keys[1], '-']
    c = [keys[2], '-']
    f = [keys[3], '-']

    for _l in l:
        for _p in p:
            for _c in c:
                for _f in f:
                    key = _l + _p + _c + _f
                    result.append(key)

    return result, score


def add_to_group_table(info_string):
    group_table = {}

    for string in info_string:
        masked_strings, score = mask_string(string)

        for k in masked_strings:
            if k in group_table.keys():
                group_table[k].append(score)

            else:
                group_table[k] = [score]

    return group_table


def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')

    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo+hi)//2

        if x <= a[mid]:
            hi = mid

        else:
            lo = mid+1

    return lo


def solution(info, query):
    info_table = add_to_group_table(info)
    answer = []

    for v in info_table.values():
        v.sort()

    for q in query:
        k, criterion = parse_info(q)

        lower_index = bisect(info_table[k], criterion)
        answer.append(len(info_table[k])-lower_index)

    return answer


if __name__ == '__main__':
    i = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
    q = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
         "- and - and - and chicken 100", "- and - and - and - 150"]

    print(solution(i, q))


    l = [1]
    print(bisect(l, 2))