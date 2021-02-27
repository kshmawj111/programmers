def kruskal(graph, nodes):
    result_tree = []
    bridges = list(reversed(graph.keys()))
    while len(result_tree) < len(nodes) - 1 and not nodes:
        minimum_cost_bridge = bridges.pop()


def solution(n, costs):
    graph = {}
    nodes = [[x] for x in range(n)]

    for c in costs:
        graph[(c[0], c[1])] = c[2]

    graph = dict(sorted(graph.items(), key=lambda x: x[1]))

    print(graph)
    return graph


if __name__ == '__main__':
    n, c = 4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    solution(n, c)
