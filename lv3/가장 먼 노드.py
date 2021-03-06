# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3
"""
    dfs로 풀 경우에 jump 횟수를 추적하기 매우 어려워져 bfs로 푸는게 제일 나아보임
"""


def convert_to_graph(vertex: list, n):
    graph = {x: [] for x in range(n+1)}
    for edge in vertex:
        s, e = edge
        graph[s].append(e)
        graph[e].append(s)

    return graph


def solution(n, edge):
    visited = [0 for _ in range(n+1)]
    graph = convert_to_graph(edge, n)
    queue = list(graph[1])

    max_jumps = 0
    visited[1] = 1
    jumps = 1

    while queue:
        for _ in range(len(queue)):
            p = queue.pop(0)

            if not visited[p]:
                visited[p] = jumps

                for x in graph[p]:
                    queue.append(x)

                max_jumps = jumps

        jumps += 1
    answer = visited.count(max_jumps)

    return answer

if __name__ == '__main__':
    n, v = 	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, v))