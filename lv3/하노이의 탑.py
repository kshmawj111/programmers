# https://programmers.co.kr/learn/courses/30/lessons/12946?language=python3

"""
    n을 오른쪽으로 보내는 문제
    -> n-1을 가운데로 보내는 문제
    -> n-2를 오른쪽으로 보내는 문제
    -> n-3을 가운데로 보내는 문제
    ...

    -> 1

"""


def hanoi(n, _from, _by, _to, _history:list):
    if n == 1:
        _history.append([_from, _to])
        print(f'{_from} to {_to}')
        return _history

    hanoi(n-1, _from, _to, _by, _history) # 기존 n-1을 가운데로
    _history.append([_from, _to])
    hanoi(n-1, _by, _from, _to, _history) # 2에 남아있는 원판을 다 3으로


def solution(n):
    history = []
    hanoi(n, 1, 2, 3, history)
    return history



if __name__ == '__main__':
    n = 3
    print(solution(n))