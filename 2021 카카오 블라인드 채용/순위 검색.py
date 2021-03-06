# https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3


"""
지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info,
개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,
각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

"""


def parse_info(string: str, delimiter=' '):
    parsed = []

    while string:
        sep = string.find(delimiter)

        if sep != -1:
            parsed.append(string[:sep])

        else:
            parsed.append(string)
            break

        string = string[sep+len(delimiter):]

    return parsed


def search_dict(info_list: list, query_dict: dict):
    search_result = info_list
    search_target = 0

    for k, v in query_dict.items():
        temp = []
        if v != '-':
            if isinstance(v, str):
                for person in search_result:
                    if person[search_target] == v:
                        temp.append(person)
            # score 비교
            else:
                for person in search_result:
                    if person[search_target] >= v:
                        temp.append(person)

            search_result = temp

        search_target += 1

    return search_result


def solution(info, query):
    answer = []
    info_list = []

    for i in info:
        parsed = parse_info(i)
        parsed[-1] = int(parsed[-1])
        info_list.append(parsed)

    for q in query:
        query_dict = {'language': [], 'position': [], 'career': [], 'food': [], 'score': []}

        filter = parse_info(q, delimiter=' and ')
        parsed = parse_info(filter[-1])
        parsed[-1] = int(parsed[-1])
        filter.remove(filter[-1])
        filter = filter + parsed

        i = 0
        for k in query_dict.keys():
            query_dict[k] = filter[i]
            i += 1

        searched = search_dict(info_list, query_dict)
        answer.append(len(searched))

    return answer


if __name__ == '__main__':
    i = ["java backend junior pizza 150","python frontend senior chicken 210",
         "python frontend senior chicken 150","cpp backend senior pizza 260",
         "java backend junior chicken 80","python backend senior chicken 50"]

    q = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250","- and backend and senior and - 150",
         "- and - and - and chicken 100","- and - and - and - 150"]

    print(solution(i, q))