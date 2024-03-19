class Graph(object):
    def __init__(self, nodes: list[str],
                 init_graph: dict[str, dict[str, int]]):
        self.nodes: list[str] = nodes
        self.graph: dict[str, dict[str, int]] = (
            Graph.construct_graph(nodes, init_graph))

    @staticmethod
    def construct_graph(nodes: list[str],
                        init_graph: dict[str, dict[str, int]]
                        ) -> dict[str, dict[str, int]]:
        graph: dict[str, dict[str, int]] = {}
        for node in nodes:
            graph[node]: dict[str, int] = {}

        graph |= init_graph

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if not graph[adjacent_node].get(node, False):
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self) -> list[str]:
        return self.nodes

    def get_outgoing_edges(self, node) -> list[str]:
        connections: list[str] = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False):
                connections.append(out_node)
        return connections

    def value(self, node1, node2) -> int:
        return self.graph[node1][node2]
