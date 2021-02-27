# https://programmers.co.kr/learn/courses/30/lessons/68646?language=python3


def solution(a):
    answer = [] # 맨 왼쪽과 오른쪽은 항상 가능
    l, r = 999999999999999999999, 9999999999999999999999999
    left = []
    right = []

    for i in range(len(a)):
        if l > a[i]:
            l = a[i]

        left.append(l)

    for i in range(len(a)-1, -1, -1):
        if r > a[i]:
            r = a[i]

        right.append(r)

    right.reverse()

    for i in range(len(a)):
        if not (left[i] < a[i] and right[i] < a[i]):
            answer.append(a[i])

    return len(answer)


if __name__ == '__main__':
    # a =	[-1, -5, 6, 8, 10, -11, -8, -20, 7 ]
    a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
    print(solution(a))