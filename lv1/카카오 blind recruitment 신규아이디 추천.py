# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
import re

# remove . at the front and back
def check_front_back(string: str, target='.'):
    if string:
        if string.startswith(target):
            string = string[len(target):]

        if string.endswith(target):
            string = string[:-len(target)]

        return string


def solution(new_id: str):
    answer = ''

    if new_id:
        temp = new_id.lower()
        matched = re.findall(r'[a-z0-9\-\_\.]', temp)

        for i in range(1, len(matched)):
            if matched[i-1] == '.' and matched[i] == matched[i-1]:
                matched[i-1] = ''

        for char in matched:
            answer += char

    answer = check_front_back(answer)

    if not answer:
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]

    elif len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    answer = check_front_back(answer)

    return answer


if __name__ == '__main__':
    new_id = "...!@BaT#*..y.abcdefghijklm"
    print(solution(new_id))