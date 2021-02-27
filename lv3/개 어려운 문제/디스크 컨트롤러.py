# https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3
import heapq
from copy import copy
"""
 작업이 비어있으면 시작 시간이 가장 작은 작업을 다음 작업으로
 작업이 바로 이어지는 경우에는 소요시간이 가장 작은 작업을 다음 작업으로
 
 문제1: 남은 태스크를 소요시간 기준을 가진 힙으로 유지하고 싶은데, jobs가 multidimensional이라서 잘 안됨. 
        print([4,2] > [3,4, 5]) -> True. 따라서 소요시간을 첫번째 원소로 두어서 heap을 구성함
        따라서 힙에서 pop하여 가져오는 경우엔 소요시간과 요청시간이 뒤바뀌어 있음.
        
 문제2: 작업이 비어있는지 차있는지 어떻게 구분해야할지 모르겠음.
 

"""


def swap_places(jobs: list):
    return list(map(lambda x: [x[1], x[0]], jobs))


def solution(jobs: list):
    REQUEST, EXECUTE_TIME = 0, 1
    length = len(jobs)
    heapq.heapify(jobs) # 요청 시간 순으로 heap 형성
    total_time, total_time_from_request = 0, 0
    delayed_task_queue = []

    while jobs or delayed_task_queue:
        if not delayed_task_queue: # 밀린 작업이 없어서 새 작업을 시작 하는 경우
            # 작업이 비어있는 경우에 행동
            r, e = heapq.heappop(jobs) # 요청 시간이 작은거 pop
            total_time = r + e
            total_time_from_request += e

        else:
            # 작업이 밀려 있는 경우, delayed_task_queue에서 값을 가져와 뽑는다
            e, r = heapq.heappop(delayed_task_queue)
            total_time += e
            total_time_from_request += total_time - r

        while jobs:
            task = heapq.heappop(jobs) # 항상 요청시간을 키로 가지는 heap 구성
            # 뽑은 태스크의 요청시간이 총 진행시간보다 이전인 경우
            if task[REQUEST] < total_time:
                heapq.heappush(delayed_task_queue, task[::-1])

            else:
                # 해당 태스크 포함, 이후 태스크는 모두 total_time 이후이므로 다시 힙에 넣어주고 중지
                heapq.heappush(jobs, task)
                break

    return int(total_time_from_request/length)





if __name__ == '__main__':
    j = [[0, 3], [5, 5], [6, 2]]
    print(solution(j))
