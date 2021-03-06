# https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3
"""
테스트 1 〉	통과 (9.18ms, 10.3MB)
테스트 2 〉	통과 (5.21ms, 10.3MB)
테스트 3 〉	통과 (6.33ms, 10.2MB)
테스트 4 〉	통과 (7.36ms, 10.3MB)
테스트 5 〉	통과 (5.88ms, 10.3MB)
테스트 6 〉	통과 (15.16ms, 10.3MB)
테스트 7 〉	통과 (15.92ms, 10.4MB)
테스트 8 〉	통과 (101.87ms, 10.4MB)
테스트 9 〉	통과 (146.99ms, 10.3MB)
테스트 10 〉	통과 (3833.31ms, 10.8MB)
테스트 11 〉	통과 (1806.55ms, 10.6MB)
테스트 12 〉	통과 (2153.65ms, 10.6MB)
테스트 13 〉	통과 (4042.58ms, 10.8MB)
테스트 14 〉	통과 (3674.47ms, 10.8MB)
테스트 15 〉	통과 (4673.89ms, 10.9MB)
테스트 16 〉	통과 (1188.05ms, 10.6MB)
테스트 17 〉	통과 (55.93ms, 10.5MB)
테스트 18 〉	통과 (22.97ms, 10.4MB)
테스트 19 〉	통과 (1.75ms, 10.3MB)
테스트 20 〉	통과 (50.15ms, 10.5MB)

"""
from itertools import combinations
import re


def make_pattern(menu_combs: tuple):
    pattern = ''

    for m in menu_combs:
        pattern += f'(?=.*{m})'

    return pattern


def set_table(orders: list, course: int):
    table = {}

    for order in orders:
        comb = combinations(order, course)

        for k in comb:
            if not k in table.keys():
                table[k] = 0

    return table


def solution(orders, course):
    answer = []
    orders = list(map(lambda x: ''.join(list(sorted(x))), orders))
    for c in course:
        table = set_table(orders, c)

        for order in orders:
            if len(order) >= c:
                for menu_combs in table.keys():
                    pattern = make_pattern(menu_combs)

                    if re.match(pattern, order):
                        table[menu_combs] += 1

        table = dict(filter(lambda x: x[1] > 1, table.items()))
        table = dict(sorted(table.items(), key=lambda x: x[1], reverse=True))
        max_appearance = None

        for k, v in table.items():
            if not max_appearance:
                max_appearance = v

            if v == max_appearance:
                answer.append(''.join(k))

    answer.sort()
    return answer


if __name__ == '__main__':
    o = ["XYZ", "XWY", "WXA"]
    c = [2,3,4]
    print(solution(o, c))
