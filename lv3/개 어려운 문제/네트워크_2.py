# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3


def dfs(root, graph, visited, network):
    visited[root] = True

    for next_node in range(len(visited)):
        if not visited[next_node]:
            if graph[root][next_node] == 1:
                network[root].append(next_node)
                graph[next_node][root] = 0
                graph[root][next_node] = 0

                dfs(next_node, graph, visited, network)


def solution(n, computers):
    visited = [False for _ in range(n)]
    network = {k: [] for k in range(n)}

    for i in range(len(computers)):
        if not visited[i]:
            dfs(i, computers, visited, network)

    keys = list(network.keys())

    for k, v in network.items():
        if v:
            for node in v:
                keys.remove(node)

    return len(keys)

if __name__ == '__main__':
    # n, c = 	3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    n, c = 5, [[1,1,1,0,0], [1, 1, 0, 0,0], [1, 0, 1,0,0], [0,0,0,1,1], [0,0,0,1,1]]
    print(solution(n,c))