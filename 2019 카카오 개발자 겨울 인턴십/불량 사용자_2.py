# https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3
import re
from itertools import product


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


def count_cases(candidates: list, matches: dict, banned_ids: list):
    result = []

    for candidate in candidates:
        # candidate : tuple
        if is_match(candidate, matches, banned_ids):
            if set(candidate) not in result:
                result.append(set(candidate))
    print(result)
    return len(result)


def is_match(candidate: tuple, matches:dict, banned_id:list):
    for i in range(len(candidate)):
        if banned_id[i] not in matches[candidate[i]]:
            return False

    return True


def solution(user_id, banned_id):
    matches = {}
    temp_match = {}

    for ban_id in banned_id:
        matched = get_matches(user_id, ban_id)
        temp_match[ban_id] = matched

        for i in matched:
            if i not in matches.keys():
                matches[i] = {ban_id}

            else:
                matches[i].add(ban_id)

    print(matches)

    temp = []
    for x in banned_id:
        temp.append(temp_match[x])

    candidates = list(filter(lambda x: len(set(x)) == len(banned_id), product(*temp)))
    answer = count_cases(candidates, matches, banned_id)
    return answer


if __name__ == '__main__':
    u, b = 	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
    print(solution(u, b))
