import pytest
from basicGraph import Node, Edge, Graph


@pytest.fixture
def graph() -> Graph:
    return Graph()


class TestNode:
    def test_node_init(self):
        node1 = Node(1)
        assert node1.val == 1
        node2 = Node(1)
        assert node2.val == 1
        node3 = Node(2)
        assert node3.val == 2

        assert node1 == node2
        assert node1 != node3


class TestEdge:
    def test_edge_init(self):
        e = Edge(1, 2)
        assert e.a == Node(1)
        assert e.b == Node(2)

    def test_edge_eq(self):
        e1 = Edge(1, 2)
        e2 = Edge(2, 1)
        e3 = Edge(2, 3)
        e4 = Edge(1, 2)

        assert e1 == e4
        assert e1 == e2
        assert e1 != e3


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

        assert graph.get_node("a").neighbours == [
            (graph.get_node("b"), Edge("a", "b"))]

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

    def test_graph_eq(self, graph):
        g2 = Graph()

        assert graph == g2

        graph.add(1, 2)
        assert graph != g2

        g2.add(1, 2)
        assert graph == g2

        g2.add(2, 3)
        assert graph != g2
