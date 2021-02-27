# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
import re


def solution(record):
    answer = []
    table = {}

    for s in record:
        l = re.split(' ', s)

        if l[0] == 'Enter':
            table[l[1]] = l[2]

        # elif l[0] == 'Leave':
        #    del table[l[1]]

        elif l[0] == 'Change':
            table[l[1]] = l[2]

    for s in record:
        l = re.split(' ', s)

        if l[0] == 'Enter':
            answer.append(f"{table[l[1]]}님이 들어왔습니다.")

        elif l[0] == 'Leave':
            answer.append(f"{table[l[1]]}님이 나갔습니다.")

    print(answer)
    return answer


if __name__ == '__main__':
    r =	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    solution(r)