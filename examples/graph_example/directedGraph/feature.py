from featurepy import Composer, Aspect, Proceed, Return, weave
from basicGraph import Node, Edge


class EdgeRefinement:
    def refine___eq__(self, original):
        def __eq__(slf, other):
            return original(slf, other) and slf.a == other.a and slf.b == other.b
        return __eq__


class GraphRefinement:
    def refine_add(self, original):
        def add(slf, a, b, *args, **kwargs):
            original(slf, a, b, *args, **kwargs)
            slf.get_node(b).neighbours.pop()

        return add


class TestEdgeRefinement:
    def refine_test_edge_eq(self, original):
        def test_edge_eq(slf):
            e1 = Edge(1, 2)
            e2 = Edge(2, 1)
            e3 = Edge(2, 3)
            e4 = Edge(1, 2)

            assert e1 == e4
            assert e1 != e2
            assert e1 != e3
        return test_edge_eq


class TestGraphRefinement:
    def refine_test_node_neighbours(self, original):
        def test_node_neighbours(self, graph):
            graph.add("a", "b")
            graph.add("c", "a")
            graph.add("a", "a")

            assert set(graph.get_node("c").neighbour_nodes()
                       ) == set([Node("a")])
            assert set(graph.get_node("b").neighbour_nodes()) == set([])
            assert set(graph.get_node("a").neighbour_nodes()) == set(
                [Node("a"), Node("b")])

        return test_node_neighbours


def select(composer: Composer):
    from basicGraph import Graph
    from basicGraph.test_graph import TestGraph

    composer.compose(GraphRefinement(), Graph)
    composer.compose(TestGraphRefinement(), TestGraph)
