import pytest
from featurepy import Aspect, Proceed, weave
from basicGraph import Edge, Node


class RepeatedEdgeError(Exception):
    "Edge already exists in simple graph"
    pass


@Aspect
def enforce_simple(slf, a, b, *args, **kwargs):
    if Edge(a, b) in slf.edges:
        raise RepeatedEdgeError("Edge already exists in simple graph")
    else:
        yield Proceed(slf, a, b, *args, **kwargs)


class EdgeRefinement:
    def refine___eq__(self, original):
        def __eq__(cls, other):
            if isinstance(other, Edge):
                return (cls.a == other.a and cls.b == other.b) or (cls.a == other.b and cls.b == other.a)
            return False

        return __eq__


class TestGraphRefinement:
    def refine_test_cycle(self, original):
        def test_cycle(slf, graph):
            print("hi")
            with pytest.raises(RepeatedEdgeError):
                graph.add("a", "b")
                graph.add("b", "a")

        return test_cycle


def select(composer):
    from basicGraph import Graph, Edge
    from basicGraph.test_graph import TestGraph

    composer.compose(EdgeRefinement(), Edge)
    # composer.compose(GraphRefinement(), Graph)
    weave(Graph, enforce_simple, methods="add")
    composer.compose(TestGraphRefinement(), TestGraph)
