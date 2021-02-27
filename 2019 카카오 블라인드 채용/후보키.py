# https://programmers.co.kr/learn/courses/30/lessons/42890?language=python3
from itertools import combinations


def convert_as_table(relation):
    table = {}

    for r in relation:
        for i in range(len(r)):
            if i in table.keys():
                table[i].append(r[i])

            else:
                table[i] = [r[i]]

    return table


def is_unique(l):
    if len(l) == len(set(l)):
        return True

    else:
        return False


def map_lists(l1, l2):
    acc = []
    if l1:
        for x in range(len(l1)):
            acc.append(l1[x]+'_'+l2[x])

        return acc

    else:
        return l2


def get_possible_values(combinations, table):
    result = []

    for comb in combinations:
        values = []
        if len(comb) > 1:
            no_keys = False
            for k in comb:
                if not k in table.keys():
                    no_keys = True
                    break

            if not no_keys:
                for i in range(-1, len(comb)-1):
                    values = map_lists(values, table[comb[i+1]])

                if is_unique(values):
                    result.append(comb)

        else:
            if is_unique(table[comb[0]]):
                result.append(comb)

    for c in result:
        for k in c:
            if k in table.keys():
                del table[k]

    return result


def solution(relation):
    answer = 0
    table = convert_as_table(relation)
    total_keys = len(table.keys())

    for num_picks in range(1, total_keys+1):
        if num_picks <= len(table):
            possible_combs = list(combinations(table.keys(), num_picks))
            found_keys = get_possible_values(possible_combs, table)
            print(found_keys)
            if len(found_keys) > 0:
                answer += 1
    return answer


if __name__ == '__main__':
    r = [["100", "a", "b", "2", '1'], ["200", "a", "b", "2", '2'], ["300", "a", "b", "3", '3'],
     ["400", "a", "b", "4", '4'], ["500", "a", "b", "3", '5'], ["600", "a", "b", "2", '3']]
    """r = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
     ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]"""
    solution(r)