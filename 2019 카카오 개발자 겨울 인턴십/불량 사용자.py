# https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3
import copy
import operator
import re
from functools import reduce


# b_id에 해당하는 아이디가 user_id_list에 몇개 있는지 반환하는 함수
def get_matches(user_id_list: list, b_id: str):
    ALL_CHAR_PATTERN = '[a-z0-9]'
    test_id = b_id.replace('*', ALL_CHAR_PATTERN)

    pattern = ''.join(test_id)

    match = []
    for x in user_id_list:
        t = re.fullmatch(pattern, x)
        if t:
            match.append(re.fullmatch(pattern, x).string)

    return match


def update_record(record, threshold):
    record[-1] += 1
    for i in range(len(record)-1, -1, -1):
        if record[i] > threshold[i]:
            record[i-1] += 1
            record[i] = 0

    return record


def count_cases(matches: list):
    counter = 0
    result = []
    threshold = [len(x)-1 for x in matches]
    record = [0 for _ in matches]

    MAX_ITER = reduce(lambda acc, x: acc*len(x), matches, 1)
    print(matches)

    while counter < MAX_ITER:
        temp = []

        for match_set_i in range(len(record)):
            a = matches[match_set_i][int(record[match_set_i])]

            if a in temp:
                break

            else:
                temp.append(a)

        if len(set(temp)) == len(matches) and set(temp) not in result:
            result.append(set(temp))

        print(result)
        counter += 1
        record = update_record(record, threshold)

    return result, len(result)


def solution(user_id, banned_id):
    matches = []
    for ban_id in banned_id:
        matched = get_matches(user_id, ban_id)
        matches.append(matched)

    matched_results, answer = count_cases(matches)
    return answer


if __name__ == '__main__':
    u, b = 	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]
    solution(u, b)
