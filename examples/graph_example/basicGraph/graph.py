from __future__ import annotations
from typing import Optional
from featurepy.feature_class import feature


@feature
class Node:
    def __init__(self, val: any):
        self.val = val
        self.neighbours: list[tuple[Node, Edge]] = []

    def neighbour_nodes(self) -> list[Node]:
        return [node for node, _ in self.neighbours]

    def neighbour_edges(self) -> list[Edge]:
        return [edge for _, edge in self.neighbours]

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f"Node({self.val})"

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.val == other.val
        return False

    def __hash__(self):
        return hash(self.val)


@feature
class Edge:
    def __init__(self, a, b):
        self.a = Node(a)
        self.b = Node(b)

    def __str__(self):
        return f"{str(self.a)}-{str(self.b)}"

    def __repr__(self):
        return f"{str(self.a)}-{str(self.b)}"

    def __eq__(cls, other):
        if isinstance(other, Edge):
            return (cls.a == other.a and cls.b == other.b) or (cls.a == other.b and cls.b == other.a)
        return False


@feature
class Graph:
    def __init__(self):
        self.edges: list[Edge] = []
        self.nodes: list[Node] = []

    def get_node(self, val) -> Optional(Node):
        node_list = list(filter(lambda x: x == Node(val), self.nodes))
        return None if node_list == [] else node_list[0]

    def add(self, a, b):
        na = Node(a)
        nb = Node(b)
        e = Edge(a, b)

        if na not in self.nodes:
            self.nodes.append(na)
        else:
            na = self.get_node(a)

        if nb not in self.nodes:
            self.nodes.append(nb)
        else:
            nb = self.get_node(b)

        self.edges.append(e)
        na.neighbours.append((nb, e))
        nb.neighbours.append((na, e))

    def __repr__(self):
        return ",".join([str(edge) for edge in self.edges])

    def __str__(self):
        return ",".join([str(edge) for edge in self.edges])
