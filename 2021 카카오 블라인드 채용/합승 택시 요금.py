# https://programmers.co.kr/learn/courses/30/lessons/72413?language=python3
"""
    Graph 탐색

    1) s에서 a, b 노드로 가는데 필요한 가장 최소의 비용 기록
    2) 그리고 추가적으로 각기 다른 노드에서 a, b로 가는 비용을 구함
    2)에서 구한 비용에 1)에서 구한 s까지 가는 비용을 더하고 
    
    위 과정 중 제일 적은 비용을 정답으로

"""
import heapq


def get_graph(n, fares: list):
    graph = {k: [] for k in range(1, n+1)}
    cost = {k: [] for k in range(1, n+1)}

    for x in fares:
        graph[x[0]].append(x[1])
        graph[x[1]].append(x[0])

        cost[(x[0], x[1])] = x[2]
        cost[(x[1], x[0])] = x[2]

    return graph, cost


def find_min_cost(n, s, graph, cost_graph):
    prev = [-1 for _ in range(n+1)]
    cost_nodes = [float('inf') for _ in range(n+1)]

    cost_nodes[s] = 0
    queue = [[0, s]]

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        for next_node in graph[current_node]:
            cost = cost_nodes[current_node] + cost_graph[(current_node, next_node)]

            # 새로구한 cost가 기존 cost보다 작으면
            if cost < cost_nodes[next_node]:
                cost_nodes[next_node] = cost
                prev[next_node] = current_node
                heapq.heappush(queue, [cost_graph[(current_node, next_node)], next_node])

    return cost_nodes, prev


def solution(n, s, a, b, fares):
    answer = float('inf')
    graph, cost_graph = get_graph(n, fares)

    start_node_cost, prev = find_min_cost(n, s, graph, cost_graph)

    for i in range(1, n + 1):
        temp = [start_node_cost[i]]
        cost, prev = find_min_cost(n, i, graph, cost_graph)
        temp.append(cost[a])
        temp.append(cost[b])

        answer = min(answer, sum(temp))

    print(answer)
    return answer


if __name__ == '__main__':
    n,s,a,b,fares = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                 [1, 6, 25]]
    # solution(n,s,a,b,fares)

    n,s,a,b,fares = 6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
    solution(n,s,a,b,fares)