# https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3
"""
테스트 1 〉	통과 (0.61ms, 10.6MB)
테스트 2 〉	통과 (1.02ms, 10.4MB)
테스트 3 〉	통과 (0.96ms, 10.5MB)
테스트 4 〉	통과 (3.19ms, 10.6MB)
테스트 5 〉	통과 (4.59ms, 10.6MB)
테스트 6 〉	통과 (8.37ms, 10.5MB)
테스트 7 〉	통과 (6.47ms, 10.8MB)
테스트 8 〉	통과 (53.02ms, 11.4MB)
테스트 9 〉	통과 (51.08ms, 11.4MB)
테스트 10 〉	통과 (51.64ms, 11.6MB)
테스트 11 〉	통과 (4.54ms, 10.6MB)
테스트 12 〉	통과 (7.64ms, 10.5MB)
테스트 13 〉	통과 (6.81ms, 10.8MB)
테스트 14 〉	통과 (26.41ms, 10.9MB)
테스트 15 〉	통과 (26.88ms, 11MB)
테스트 16 〉	통과 (4.73ms, 10.6MB)
테스트 17 〉	통과 (7.32ms, 10.6MB)
테스트 18 〉	통과 (26.22ms, 10.9MB)

효율성  테스트
테스트 1 〉	통과 (975.81ms, 42.3MB)
테스트 2 〉	통과 (988.39ms, 42.4MB)
테스트 3 〉	통과 (979.89ms, 42.5MB)
테스트 4 〉	통과 (992.39ms, 42.4MB)

"""
import re


def parse_info(string: str, for_query=False):
    parsed = re.split(' and | ', string)
    score = int(parsed[-1])
    parsed = parsed[:-1]
    key = ''

    if not for_query:
        for w in range(len(parsed)-1):
            key += parsed[w] + '/'

        key += parsed[-1]

    else:
        for w in parsed:
            key += w

    return key, score


def initialize_group_table():
    group_table = {}

    l = ['java', 'python', 'cpp', '-']
    p = ['backend', 'frontend', '-']
    c = ['junior', 'senior', '-']
    f = ['pizza', 'chicken', '-']

    for _l in l:
        for _p in p:
            for _c in c:
                for _f in f:
                    key = _l + _p + _c + _f
                    group_table[key] = []

    return group_table


def mask_string(key: str):
    key = re.split('/', key)
    result = []
    l = [key[0], '-']
    p = [key[1], '-']
    c = [key[2], '-']
    f = [key[3], '-']

    for _l in l:
        for _p in p:
            for _c in c:
                for _f in f:
                    key = _l + _p + _c + _f
                    result.append(key)

    return result


def add_to_group_table(info_string):
    group_table = initialize_group_table()

    for string in info_string:
        key, score = parse_info(string)
        masked_strings = mask_string(key)

        for k in masked_strings:
            group_table[k].append(score)

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
        k, criterion = parse_info(q, for_query=True)

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