# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3


def solution(n: list, t):
    i = 0
    queue = [0]
    print(queue)

    while queue and i < len(n):
        temp = []

        while queue:
            popped = queue.pop()
            # neg = f'{popped}-{n[i]}'
            # pos = f'{popped}+{n[i]}'
            neg = popped - n[i]
            pos = popped + n[i]
            temp.insert(0, pos)
            temp.insert(0, neg)

        queue = temp
        i += 1
        print(queue)

    counts = queue.count(t)
    print(counts)
    return counts


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    t = 3

    solution(numbers, t)