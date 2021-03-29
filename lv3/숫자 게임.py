# https://programmers.co.kr/learn/courses/30/lessons/12987?language=python3


def solution(A, B):
    A.sort()
    B.sort()
    answer = 0

    for i in range(len(A)-1, -1, -1):
        last = B[-1]

        if last > A[i]:
            B.pop()
            answer += 1

        elif last == A[i]:
            B.pop()

    print(answer)
    return answer


if __name__ == '__main__':
    a, b = 	[7,6,6,2], [8,6,3,2]
    solution(a, b)