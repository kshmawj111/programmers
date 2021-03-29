import heapq


def heap_insert(num, heap: list):
    # min heap을 기준으로 해서 넣음
    heapq.heappush(heap, (num, -num))


def heap_pop_max(heap: list):
    heapq.heapify(heap)
    t =  heapq.heappop(heap)[1]
    return t


def heap_pop_min(heap: list):
    heapq.heapify(heap)
    t = heapq.heappop(heap)[0]
    return t


def solution(operations):
    heap = []

    for op in operations:
        temp = op.split(' ')
        inst = temp[0]
        num = int(temp[1])

        if inst == 'I':
            heap_insert(num, heap)

        elif inst == 'D' and heap:
            if num == -1:
                heap = list(map(lambda x: (x[0], -x[0]), heap))
                heap_pop_min(heap)
                heap = list(map(lambda x: (x[0], -x[0]), heap))

            elif num == 1:
                heap = list(map(lambda x: (-x[0], x[0]), heap))
                heap_pop_max(heap)
                heap = list(map(lambda x: (-x[0], x[0]), heap))

    print(heap)
    if not heap:
        return [0, 0]

    else:
        return [heapq.nlargest(1, heap)[0][0], heapq.nsmallest(1, heap)[0][0]]



if __name__ == '__main__':
    '''o = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    print(solution(o))'''

    o = 	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(o))