# https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3
import copy


def check_backward(n, point, d, weak: list):
    converted_weak = list(map(lambda x: x+n if x <= point else x, weak))
    cc_interval = [n+point-d, n+point]
    work_done = []

    for weak_point in converted_weak:
        if cc_interval[0] <= weak_point <= cc_interval[1]:
            work_done.append(weak_point % n)

    return work_done


def check_forward(n, point, d, weak: list):
    converted_weak = list(map(lambda x: x + n if x < point else x, weak))
    work_interval = [point, point+d]
    work_done = []

    for weak_point in converted_weak:
        if work_interval[0] <= weak_point <= work_interval[1]:
            work_done.append(weak_point % n)

    return work_done


"""def get_max_dist(n, weak: list):
    result = {}

    for i in range(len(weak)):
        current_weak = weak[i]
        idx = bisect(weak, current_weak+(n/2))
        c_w_far_weak = weak[idx-1]
        cc_w_far_weak = weak[idx]

        result[current_weak] = min(c_w_far_weak-current_weak, n + current_weak - cc_w_far_weak)"""


def get_max_dist(n, weak: list):
    result = {}

    for i in range(len(weak)):
        current_point = weak[i]
        clock_wise_target = weak[i-1]
        c_clock_wise_target = weak[(i+1)% len(weak)]

        c_w_d = n - (current_point-clock_wise_target)
        cc_w_d = (n+current_point) - c_clock_wise_target

        result[current_point] = min(c_w_d, cc_w_d)

    return result


def co_work_case(n, dist, weak):
    """
        weak 원소에 한 명 배치한 후,
        그 한 명으로 커버 안되면 다음 사람 투입

        위의 과정 반복한 다음 최종 명수 기록

        원소에 배치 된 사람은 시계, 반시계 방향으로 조사하여 최대한 많은 weak 커버할 수 있는 방법 선택.
        방법을 선택하면 선택된 방법에 포함되는 weak은 모두 제거

    """
    table = {}

    # 여러명이 필요한 경우
    for point in weak:
        min_workers = 0
        c_weak = copy.deepcopy(weak)

        for worker in dist:
            b = check_backward(n, point, worker, c_weak)
            f = check_forward(n, point, worker, c_weak)

            if len(b) >= len(f):
                maximum = b

            else:
                maximum = f

            if maximum:
                min_workers += 1

            c_weak = list(set(c_weak) - set(maximum))
            c_weak.sort()

            if not c_weak:
                break

            else:
                point = c_weak[0]

        if len(c_weak) < 1:
            table[point] = min_workers

        else:
            # 해당 포인트에서는 작업을 완료할 수 없을 때
            table[point] = len(dist) + 1
        print(table)
    return table


def solution(n, weak, dist):
    dist.sort()
    table = co_work_case(n, dist, weak)
    print(table)
    if sum(table.values()) == 0: # 작업 수행 불가
        return -1
    else:
        return min(table.values())



if __name__ == '__main__':
    n, w, d = 	12, [1, 5, 6, 10], [1, 2, 3, 4]
    print(solution(n,w,d))