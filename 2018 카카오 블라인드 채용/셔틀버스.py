# https://programmers.co.kr/learn/courses/30/lessons/17678?language=python3
from collections import deque
from datetime import timedelta, datetime


class Bus:
    def __init__(self, size):
        self.max_size = size
        self.container = []
        self.container_debug = []
        self.current_size = 0

    def __str__(self):
        return self.container

    def take_bus(self, e):
        if self.current_size < self.max_size:
            self.container.append(e)
            e = e.strftime("%H:%M")
            self.container_debug.append(e)
            self.current_size += 1
            return True

        else:
            return False

    def is_full(self):
        return self.current_size >= self.max_size

    def last_person(self):
        if self.container:
            return self.container[-1]


def solution(n, t, m, timetable):
    for x in range(len(timetable)):
        if timetable[x] == '24:00':
            timetable[x] = '00:00'

    crew_queue = deque(sorted(timetable))
    crew_queue = deque(map(lambda x: datetime.strptime(x, '%H:%M'), crew_queue))

    on_board_table = {}
    initial_bus_time= datetime.strptime("09:00", '%H:%M')
    interval = timedelta(minutes=t)
    temp = initial_bus_time

    # n번 동안
    for _ in range(n):
        on_board_table[temp.strftime("%H:%M")] = Bus(m)

        # queue에 있느 사람 버스에 태우기
        while crew_queue:
            target = crew_queue[0]

            if target <= temp:
                inserted = on_board_table[temp.strftime("%H:%M")].take_bus(target)

                # 잘 들어갔으면
                if inserted:
                    crew_queue.popleft() # 팝해서 제거

                # 꽉차서 못 들어갔으면 중지
                else:
                    break

            else: break

        temp += interval

    for k, v in on_board_table.items():
        print(f'{k}: {v.container_debug}', end=' ')

    # 마지막 버스가 다 안 찼으면 버스 오는 시간으로
    # 마지막 버스가 다 찼다면 버스 탄 사람 중 가장 늦은 사람보다 1분 앞서서
    last_bus_time = list(on_board_table.keys())[-1]
    last_bus = on_board_table[last_bus_time]

    if not last_bus.is_full():
        answer = last_bus_time

    else:
        answer = last_bus.last_person() - timedelta(minutes=1)
        answer = answer.strftime("%H:%M")

    return answer

if __name__ == '__main__':
    """n, t, m, tt = 1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]
    print(solution(n, t, m, tt))

    n, t, m, tt = 	2, 10, 2, ["09:10", "09:09", "08:00"]
    print(solution(n, t, m, tt))

    n, t, m, tt = 	2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]
    print(solution(n, t, m, tt))

    n, t, m, tt = 		1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]
    print(solution(n, t, m, tt))

    n, t, m, tt = 1, 1, 1, ["23:59"]
    print(solution(n, t, m, tt))

    n, t, m, tt = 		10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
    print(solution(n, t, m, tt))"""

    n, t, m, tt = 1, 1, 1, ["24:00"]
    print(solution(n, t, m, tt))