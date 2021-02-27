# https://programmers.co.kr/learn/courses/30/lessons/62048?language=python3
import math


def solution_내꺼(w, h):
    answer = 0

    if w == h: # 정사각형
        answer = w*(w-1)

    else: # 직사각형
        whole = w * h
        if h > w:
            temp = h
            h = w
            w = temp

        broken = math.ceil(w / h) * h

        if math.gcd(w, h) == 1:
            broken += (h // 2)

        answer = whole - broken

    return answer

def other(w,h):
    whole = w * h
    broken = w + h - math.gcd(w, h)

    return whole - broken

if __name__ == '__main__':
    w = [11, 11, 12, 11, 12, 7]
    h = [10, 13, 13, 12, 11, 3]

    for _w, _h in zip(w, h):
        print(solution_내꺼(_w, _h))
        print(other(_w, _h))