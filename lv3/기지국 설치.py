# https://programmers.co.kr/learn/courses/30/lessons/12979?language=python3
import math


def min_base_stations(length_of_apt, w):
    min_block = w*2 + 1
    return math.ceil(length_of_apt/min_block)


def solution(n, stations, w):
    answer = 0
    no_reach = []
    start = 1
    i = 0

    while start <= n:
        if i < len(stations):
            x = stations[i]
            temp = [start, x-w-1]
            no_reach.append(temp)
            start = x+w+1
            i += 1

        else:
            temp = [start, n]
            no_reach.append(temp)
            start = n + 1

    for block in no_reach:
        area_to_cover = block[1] - block[0] + 1
        answer += min_base_stations(area_to_cover, w)

    print(no_reach)
    return answer

if __name__ == '__main__':
    n, staions, w = 10, [3, 8], 1
    print(solution(n, staions, w))
    n, staions, w = 11, [4,11], 1
    print(solution(n, staions, w))
