# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3
import heapq


def solution_sort(scoville: list, K: int):
    answer = 0
    scoville.sort(reverse=True)

    while len(scoville) > 1:
        min_scoville = scoville.pop()
        next_min_scoville = scoville.pop()
        mixed_scoville = min_scoville + (next_min_scoville * 2)

        scoville.append(mixed_scoville)
        answer += 1

        scoville.sort(reverse=True)

        if scoville[-1] >= K:
            break

    if scoville[-1] < K:
        return -1

    else:
        return answer
"""

테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (3.12ms, 10.2MB)
테스트 7 〉	통과 (2.07ms, 10.3MB)
테스트 8 〉	통과 (0.16ms, 10.2MB)
테스트 9 〉	통과 (0.13ms, 10.2MB)
테스트 10 〉	통과 (1.68ms, 10.3MB)
테스트 11 〉	통과 (1.01ms, 10.2MB)
테스트 12 〉	통과 (4.79ms, 10.2MB)
테스트 13 〉	통과 (2.18ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (2.28ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)

"""


def use_heap(scoville: list, K: int):
    heapq.heapify(scoville)
    answer = 0
    # print(scoville)

    while len(scoville) > 1:
        min_scoville = heapq.heappop(scoville)
        next_min_scoville = heapq.heappop(scoville)
        mixed_scoville = min_scoville + (next_min_scoville * 2)

        heapq.heappush(scoville, mixed_scoville)
        answer += 1
        # print(scoville)

        if scoville[0] >= K:
            break

    if scoville[-1] < K:
        return -1

    else:
        return answer
"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.28ms, 10.2MB)
테스트 6 〉	통과 (3.74ms, 10.1MB)
테스트 7 〉	통과 (2.96ms, 10.2MB)
테스트 8 〉	통과 (0.16ms, 10.2MB)
테스트 9 〉	통과 (0.12ms, 10.1MB)
테스트 10 〉	통과 (2.24ms, 10.2MB)
테스트 11 〉	통과 (0.78ms, 10.2MB)
테스트 12 〉	통과 (7.68ms, 10.3MB)
테스트 13 〉	통과 (4.22ms, 10.2MB)
테스트 14 〉	통과 (0.03ms, 10.2MB)
테스트 15 〉	통과 (4.53ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.1MB)
"""


def without_sort(scoville: list, K: int):
    answer = 0

    while len(scoville) > 1:
        min_scoville = min(scoville)
        scoville.remove(min_scoville)

        next_min_scoville = min(scoville)
        scoville.remove(next_min_scoville)

        mixed_scoville = min_scoville + (next_min_scoville * 2)

        scoville.append(mixed_scoville)
        answer += 1

        if min(scoville) >= K:
            break

    if min(scoville) < K:
        return -1

    else:
        return answer


if __name__ == '__main__':
    s = [1, 2, 3, 9, 10, 12]
    k = 7
    print(without_sort(s, k))