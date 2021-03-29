# https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3
from copy import copy


def cal_min_dist(point_a, point_b, n):
    ma = max(point_a, point_b)
    mi = min(point_a, point_b)

    clock = ma - mi
    counter_clock = n+mi - ma

    return min(clock, counter_clock)


def cal_table(n, weak: list):
    table = {}

    for i in range(len(weak)):
        cur = weak[i]
        next = weak[(i+1)%len(weak)]
        dist = cal_min_dist(cur, next, n)
        table[(cur, next)] = dist

    return table


def remove_points(s, dist, weak:list):
    for x in weak[:]:
        if s <= x <= s+dist:
            weak.remove(x)


def cal_required_workers(n, sp, table:dict, weak:list, dist):
    c_table = copy(table)
    c_weak = copy(weak)

    num_worker = 0
    target_point = sp
    dist_idx = len(dist) - 1

    while c_table and dist_idx > -1:
        max_dist = dist[dist_idx]
        prev_len = len(c_weak)

        for k, v in c_table.items():
            if k[0] == target_point and v <= max_dist:
                num_worker += 1

                remove_points(k[0], k[1], c_weak)
                c_table = cal_table(n, c_weak)
                dist_idx -= 1

                break

        if prev_len == len(c_weak): # 바뀐게 없음
            return -1

        elif prev_len != len(c_weak) and c_table:
            target_point = list(c_table.keys())[0][0]

    if not c_weak:
        return num_worker


def solution(n, weak, dist):
    answer = float('inf')
    dist.sort()
    table = cal_table(n, weak)
    print(table)

    for sp in weak:
        workers = cal_required_workers(n, sp, table, weak, dist)

        if workers != -1:
            if workers < answer:
                answer = workers

    return answer



if __name__ == '__main__':
    n, w, d = 		12, [1, 3, 4, 9, 10], [3, 5, 7]
    print(solution(n,w,d))