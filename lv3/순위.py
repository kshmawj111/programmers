# https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3
"""
    각 경기 결과를 승자를 루트로 하는 트리로 형성하기
    union-find 알고리즘 사용

"""


def find_parent(node, parent):
    if parent[node] != node:
        parent[node] = find_parent(parent[node], parent)

    return parent[node]


def union(winner, loser, parent, rank):
    winner_root = find_parent(winner, parent)
    loser_root = find_parent(loser, parent)

    # 다른 집합에 속해 있으면
    if winner_root != loser_root:
        parent[loser_root] = winner_root


def solution(n, results):
    answer = 0
    parent = [x for x in range(n+1)]
    rank = [0 for x in range(n+1)]

    for r in results:
        w, l = r
        union(w, l, parent, rank)

    print(parent)
    print(rank)

    return answer


if __name__ == '__main__':
    n, r = 	5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, r))

