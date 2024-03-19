from sys import maxsize


def bellman_ford(graph: list[list[int]], v: int, e: int, src: int):
    dis: list[int] = [maxsize] * v

    dis[src] = 0

    for i in range(v - 1):
        for j in range(e):
            if dis[graph[j][0]] + \
                    graph[j][2] < dis[graph[j][1]]:
                dis[graph[j][1]] = dis[graph[j][0]] + \
                                   graph[j][2]

    for i in range(e):
        x: int = graph[i][0]
        y: int = graph[i][1]
        weight: int = graph[i][2]
        if dis[x] != maxsize and dis[x] + \
                weight < dis[y]:
            print("Graph contains negative weight cycle")

    print("Vertex Distance from Source")
    for i in range(v):
        print(f"{i}, {dis[i]}")


# Driver Code
def main():
    V = 5  # Number of vertices in graph
    E = 8  # Number of edges in graph

    # Every edge has three values (u, v, w) where
    # the edge is from vertex u to v. And weight
    # of the edge is w.
    graph = [
        [0, 1, -1],
        [0, 2, 4],
        [1, 2, 3],
        [1, 3, 2],
        [1, 4, 2],
        [3, 2, 5],
        [3, 1, 1],
        [4, 3, -3]
    ]
    bellman_ford(graph, V, E, 0)


if __name__ == "__main__":
    main()
