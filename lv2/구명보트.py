# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3


def solution(people: list, limit):
    num_boat = 0
    people.sort()
    small_i = 0
    big_i = len(people) - 1

    while small_i <= big_i:
        if people[small_i] + people[big_i] <= limit:
            num_boat += 1
            small_i += 1
            big_i -= 1

        else:
            num_boat += 1
            big_i -= 1
    return num_boat

if __name__ == '__main__':
    p = [70, 80, 50]
    l = 100
    print(solution(p, l))

    p = [70, 50, 80]
    l = 100
    print(solution(p, l))

    p = [5,6,7,8]
    l = 12
    print(solution(p, l))

    p = [40, 50, 60, 70]
    l = 110
    print(solution(p, l))

