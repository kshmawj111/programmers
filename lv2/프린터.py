# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

def solution(priorities: list, location):
    answer = 0
    spool_queue = [(index, priority) for index, priority in zip(range(len(priorities)), priorities)]
    output = []

    while spool_queue:
        current_doc = spool_queue.pop(0)

        # 만약 큐가 비어있지 않고 현재 문서보다 중요도가 높은 문서가 인쇄열에 있으면
        if spool_queue and current_doc[1] < max(spool_queue, key=lambda x: x[1])[1]:
            # 대기목록 뒤로 넣음
            spool_queue.append(current_doc)

        else:
            output.append(current_doc)
            if current_doc[0] == location:
                answer = len(output)

    return answer

if __name__ == '__main__':
    p = [2, 1, 3, 2]
    l = 2
    print(solution(p, l))

    p = [1, 1, 9, 1, 1, 1]
    l = 0
    print(solution(p, l))
