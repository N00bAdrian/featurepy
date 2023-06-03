import pytest
from basicGraph import Node, Edge, Graph


@pytest.fixture
def new_graph():
    g = Graph()
    return g


class TestEdge:
    def test_go_from(self):
        edge = Edge("a", "b")

        assert edge.go_from("a") == "b"
        assert edge.go_from("b") == "a"
        assert edge.go_from("c") is None


class TestGraph:
    def test_init_graph(self, new_graph):
        assert new_graph.edges == []
        assert new_graph.nodes == []

    def test_loop(self, new_graph):
        new_graph.add("a", "a")

        assert len(new_graph.nodes) == 1
        assert len(new_graph.edges) == 1
        assert str(new_graph) == "a-a"

    def test_insert_edge(self, new_graph):
        new_graph.add("a", "b")

        assert len(new_graph.nodes) == 2
        assert len(new_graph.edges) == 1
        assert str(new_graph) == "a-b"

    def test_cycle(self, new_graph):
        new_graph.add("a", "b")
        new_graph.add("b", "a")

        assert len(new_graph.nodes) == 2
        assert len(new_graph.edges) == 2
        assert str(new_graph) == "a-b,b-a"

    def test_nodes_from(self, new_graph):
        new_graph.add("a", "b")
        new_graph.add("a", "c")
        new_graph.add("a", "a")

        assert all([len(new_graph.nodes_from(node.val))
                   > 0 for node in new_graph.nodes])

        assert set(new_graph.nodes_from("c")) == set(["a"])
        assert set(new_graph.nodes_from("b")) == set(["a"])
        assert set(new_graph.nodes_from("a")) == set(["a", "b", "c"])
