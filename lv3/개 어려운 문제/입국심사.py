# https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3


def solution(n, times):
    times.sort()
    answer = 0
    min_time = 1
    max_time = times[-1]*n + 1

    while min_time <= max_time:
        next_time = (min_time + max_time)//2
        total_inspections = 0

        for t in times:
            total_inspections += next_time // t

            if total_inspections >= n:
                break

        if total_inspections >= n:
            answer = next_time
            max_time = next_time - 1

        else:
            min_time = next_time + 1

    return answer


if __name__ == '__main__':
    n, t = 	6, [7, 10]
    solution(n, t)

