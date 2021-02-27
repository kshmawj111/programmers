# https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3


def validate_skill_order(extracted_list: list):
    result = True
    compared = 0

    for order in extracted_list:
        if order == compared:
            compared += 1

        else:
            result = False

    return result


def solution(skill, skill_trees):
    answer = 0
    orders = [x for x in skill]
    skill_trees = [list(x) for x in skill_trees]
    result = []

    for skill_tree in skill_trees:
        extracted = []  # 순서에 상관 있는 스킬들의 인덱스만 뽑아서 저장하는 배열
        for skill in skill_tree:
            try:
                extracted.append(orders.index(skill))

            except:
                continue

        result.append(validate_skill_order(extracted))

    answer = sum(result)
    return answer


if __name__ == '__main__':
    s = 'CBD'
    t = ["BACDE", "CBADF", "AECB", "BDA"]
    solution(s, t)