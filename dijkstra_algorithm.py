import sys

from graph import Graph


def dijkstra_algorithm(
        graph: Graph, start_node: str
        ) -> tuple[dict[str, str | None], dict[str, int]]:
    unvisited_nodes: list[str] = list(graph.get_nodes())
    shortest_path: dict[str, int] = {}
    previous_nodes: dict[str, str | None] = {}

    max_value: int = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node: str | None = None
        for node in unvisited_nodes:
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors: list[str] = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value: int = (shortest_path[current_min_node] +
                                    graph.value(current_min_node, neighbor))
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_result(previous_nodes: dict[str, str | None],
                 shortest_path: dict[str, int],
                 start_node: str, target_node: str) -> None:
    path: list[str] = []
    node: str = target_node

    while node != start_node:
        path.append(node)
        node: str = previous_nodes[node]

    path.append(start_node)

    print(
        f"Найден следующий лучший маршрут с ценностью \
        {shortest_path[target_node]}.")
    print(" -> ".join(reversed(path)))


def main() -> None:
    cities: list[str] = [
        "Reykjavik", "Oslo",
        "Moscow", "London",
        "Rome", "Berlin",
        "Belgrade", "Athens"
    ]

    start_node: str = "Reykjavik"
    target_node: str = "Belgrade"

    init_graph: dict[str, dict[str, int]] = {}

    for city in cities:
        init_graph[city]: dict[str, int] = {}

    init_graph["Reykjavik"]["Oslo"] = 5
    init_graph["Reykjavik"]["London"] = 4
    init_graph["Oslo"]["Berlin"] = 1
    init_graph["Oslo"]["Moscow"] = 3
    init_graph["Moscow"]["Belgrade"] = 5
    init_graph["Moscow"]["Athens"] = 4
    init_graph["Athens"]["Belgrade"] = 1
    init_graph["Rome"]["Berlin"] = 2
    init_graph["Rome"]["Athens"] = 2
    graph: Graph = Graph(cities, init_graph)

    previous_nodes, shortest_path = (
        dijkstra_algorithm(graph=graph, start_node=start_node))
    print_result(previous_nodes, shortest_path,
                 start_node=start_node, target_node=target_node)


if __name__ == "__main__":
    main()
