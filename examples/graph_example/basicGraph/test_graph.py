import pytest
from basicGraph import Node, Edge, Graph


@pytest.fixture
def graph() -> Graph:
    return Graph()


class TestEdge:
    def test_edge_init(self):
        e = Edge(1, 2)
        assert e.a == Node(1)
        assert e.b == Node(2)


class TestGraph:
    def test_init_graph(self, graph):
        assert graph.edges == []
        assert graph.nodes == []

    def test_loop(self, graph):
        graph.add("a", "a")

        assert len(graph.nodes) == 1
        assert len(graph.edges) == 1
        assert str(graph) == "a-a"

    def test_insert_edge(self, graph):
        graph.add("a", "b")

        assert len(graph.nodes) == 2
        assert len(graph.edges) == 1
        assert str(graph) == "a-b"

    def test_cycle(self, graph):
        graph.add("a", "b")
        graph.add("b", "a")

        assert len(graph.nodes) == 2
        assert len(graph.edges) == 2
        assert str(graph) == "a-b,b-a"

    def test_node_neighbours(self, graph):
        graph.add("a", "b")
        graph.add("c", "a")
        graph.add("a", "a")

        assert all([len(node.neighbours) > 0 for node in graph.nodes])

        assert set(graph.get_node("c").neighbour_nodes()) == set([Node("a")])
        assert set(graph.get_node("b").neighbour_nodes()) == set([Node("a")])
        assert set(graph.get_node("a").neighbour_nodes()) == set(
            [Node("a"), Node("b"), Node("c")])
