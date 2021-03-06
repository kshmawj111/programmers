# https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3


def find_parent(node, parent):
    if parent[node] != node:
        parent[node] = find_parent(parent[node], parent)

    return parent[node]


def union(node1, node2, parent, rank):
    root1 = find_parent(node1, parent)
    root2 = find_parent(node2, parent)

    # 다른 집합에 속해 있으면
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1

        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1


def solution(n: int, costs: list):
    cost = 0
    graph = {}
    parent = {} # 트리의 루트 저장
    rank = {} # 트리 높이 저장

    for c in costs:
        graph[(c[0], c[1])] = c[2]

    graph = dict(sorted(graph.items(), key=lambda x: x[1]))

    # initilalize
    for node in range(n):
        parent[node] = node
        rank[node] = 0 # 트리 높이를 모두 0으로 초기화

    minimum_spanning_tree = []

    # 간선 연결 (사이클 없게)
    for edge in graph.keys():
        start_node, end_node = edge
        if find_parent(start_node, parent) != find_parent(end_node, parent):
            union(start_node, end_node, parent, rank)
            minimum_spanning_tree.append(edge)
            cost += graph[edge]

    return cost


if __name__ == '__main__':
    n, c = 	4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    solution(n, c)
