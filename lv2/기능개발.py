# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3


def solution(progresses: list, speeds):
    answer = []

    while progresses:
        for pi in range(len(progresses)):
            progresses[pi] += speeds[pi]

        completed_tasks = 0

        while completed_tasks < len(progresses):
            if progresses[completed_tasks] >= 100:
                completed_tasks += 1

            else:
                break

        if completed_tasks > 0:
            progresses = progresses[completed_tasks:]
            speeds = speeds[completed_tasks:]
            answer.append(completed_tasks)

    print(answer)
    return answer


if __name__ == '__main__':
    p = [93, 30, 55]
    s = [1, 30, 5]

    solution(p, s)

    p = [95, 90, 99, 99, 80, 99]
    s = [1, 1, 1, 1, 1, 1]

    solution(p, s)
