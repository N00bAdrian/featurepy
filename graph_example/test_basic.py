from featuremonkey import select
import pytest

select("basicGraph")
from basicGraph import *

@pytest.fixture
def new_graph():
    g = Graph()
    g.nodes = []
    g.edges = []
    return g

class TestBasicGraph:
    def test_init_graph(self, new_graph):
        assert new_graph.edges == []
        assert new_graph.nodes == []

    def test_loop(self, new_graph):
        new_graph.add(Node("a"), Node("a"))

        assert len(new_graph.nodes) == 1
        assert len(new_graph.edges) == 1
        assert str(new_graph) == "a-a"

    def test_insert_edge(self, new_graph):
        new_graph.add(Node("a"), Node("b"))

        assert len(new_graph.nodes) == 2 
        assert len(new_graph.edges) == 1
        assert str(new_graph) == "a-b"

    def test_cycle(self, new_graph):
        new_graph.add(Node("a"), Node("b"))
        new_graph.add(Node("b"), Node("a"))

        assert len(new_graph.nodes) == 2
        assert len(new_graph.edges) == 2
        assert str(new_graph) == "a-b,b-a"
