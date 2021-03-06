# https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3
"""
테스트 1 〉	통과 (0.25ms, 10.5MB)
테스트 2 〉	통과 (0.25ms, 10.6MB)
테스트 3 〉	통과 (0.94ms, 10.5MB)
테스트 4 〉	통과 (7.54ms, 10.9MB)
테스트 5 〉	통과 (21.61ms, 11MB)
테스트 6 〉	통과 (43.23ms, 11MB)
테스트 7 〉	통과 (23.25ms, 11.6MB)
테스트 8 〉	통과 (103.87ms, 13.9MB)
테스트 9 〉	통과 (110.09ms, 14MB)
테스트 10 〉	통과 (108.83ms, 14.1MB)
테스트 11 〉	통과 (20.63ms, 10.9MB)
테스트 12 〉	통과 (42.17ms, 11MB)
테스트 13 〉	통과 (23.50ms, 11.7MB)
테스트 14 〉	통과 (89.84ms, 12.4MB)
테스트 15 〉	통과 (96.84ms, 12.4MB)
테스트 16 〉	통과 (20.63ms, 10.9MB)
테스트 17 〉	통과 (42.20ms, 11.1MB)
테스트 18 〉	통과 (92.75ms, 12.4MB)
"""
import re
from copy import copy


def parse_info(string_long: str):
    parsed_dict = {}
    parse_format_base = {'language': '', 'position': '', 'career': '', 'food': ''}
    keys = list(parse_format_base.keys())

    for string_idx in range(len(string_long)):
        parse_format = copy(parse_format_base)
        string = string_long[string_idx]
        parsed = re.split(' and | ', string)
        parsed[-1] = int(parsed[-1])

        for i in range(len(parsed)):
            parse_format[keys[i]] = parsed[i]

        parsed_dict[string_idx] = parse_format

    return parsed_dict


def search_dict(info_dict: dict, query_dict: dict):
    from copy import copy
    searched_result = copy(info_dict)

    for k, v in query_dict.items():
        if v != '-':
            keys = list(searched_result.keys())

            if isinstance(v, str):
                for p in keys:
                    if searched_result[p][k] != v:
                        del searched_result[p]

            else:
                for p in keys:
                    if searched_result[p][k] < v:
                        del searched_result[p]

    return searched_result


def solution(info, query):
    answer = []
    info_dict = parse_info(info)
    query_dict = parse_info(query)

    for _, v in query_dict.items():
        searched = search_dict(info_dict, v)
        answer.append(len(searched))

    return answer


if __name__ == '__main__':
    i = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
    q = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
         "- and - and - and chicken 100", "- and - and - and - 150"]

    print(solution(i, q))