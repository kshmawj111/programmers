# https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3
from collections import defaultdict


def convert_as_graph(tickets):
    graph = defaultdict(list)

    for e in tickets:
        k, v = e
        graph[k].append(v)

    for k, v in graph.items():
        graph[k] = list(sorted(v, reverse=True))

    return graph


def dfs(graph):
    path = []
    stack = ["ICN"]

    while stack:
        p = stack[-1]

        if p not in graph or not graph[p]:
            path.append(stack.pop())

        else:
            stack.append(graph[p].pop())

    path.reverse()

    return path


def solution(tickets):
    graph = convert_as_graph(tickets)
    answer = dfs(graph)
    print(answer)
    return answer


if __name__ == '__main__':
    #t =  [['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]

    #solution(t)
    t = 	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    solution(t)