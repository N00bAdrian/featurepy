from featurepy import Composer
from basicGraph import Node, Edge
# from fixtures import new_graph


class EdgeRefinement:
    def refine_go_from(self, original):
        def go_from(slf, a):
            return slf.b.val if Node(a) == slf.a else None

        return go_from


class TestEdgeRefinement:
    def refine_test_go_from(self, original):
        def test_go_from(slf):
            edge = Edge("a", "b")

            assert edge.go_from("a") == "b"
            assert edge.go_from("b") is None
            assert edge.go_from("c") is None

        return test_go_from


class TestGraphRefinement:
    def refine_test_nodes_from(self, original):
        def test_nodes_from(slf, new_graph):
            new_graph.add("a", "b")
            new_graph.add("c", "a")
            new_graph.add("a", "a")

            assert set(new_graph.nodes_from("c")) == set(["a"])
            assert set(new_graph.nodes_from("b")) == set([])
            assert set(new_graph.nodes_from("a")) == set(["a", "b"])

        return test_nodes_from


def select(composer: Composer):
    from basicGraph import Edge
    from fixtures import TestEdge, TestGraph

    composer.compose(EdgeRefinement(), Edge)
    composer.compose(TestEdgeRefinement(), TestEdge)
    composer.compose(TestGraphRefinement(), TestGraph)
