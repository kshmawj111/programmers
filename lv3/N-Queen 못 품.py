# https://programmers.co.kr/learn/courses/30/lessons/12952?language=python3
"""
    0,0 부터 시작해서 다음 열에 퀸을 놓을 수 있다면 해당 항목을 path 스택에 삽입
    놓을 수 없다면 backtrack


"""
def is_valid(path: list, next_val):
    n = len(path)-1
    if next_val in path:
        return False

    if path[n] - 1 <= next_val <= path[n] + 1:
        return False

    return True


def get_possible_loc(path, n):
    candidates = [x for x in range(n) if x not in path]
    possibles = []
    for c in candidates:
        if is_valid(path, c):
            possibles.append(c)

    return possibles

def solution(n):
    answer = 0
    path_roots = [x for x in range(n)]
    initial_state = []
    path = []

    for root in path_roots:
        path = []
        path.append(root)
        initial_state = [-1] * n
        possibles = [-1] * n

        while path:
            next_pos = (possibles[len(path)-1] + 1) % n

            if is_valid(path, next_pos):
                path.append(next_pos)
                initial_state[len(path) -1] = next_pos

            else:
                if next_pos == initial_state[len(path)-1]:
                    path.pop()
                    initial_state[len(path)] = -1
                    possibles[len(path)] = -1

                possibles[len(path)-1] += 1

            if len(path) == n:
                answer += 1

    return answer


if __name__ == '__main__':
    print(solution(4))