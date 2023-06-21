import pytest
from featurepy import Aspect, Proceed, weave
from basicGraph import Edge, Node


class RepeatedEdgeError(Exception):
    "Edge already exists in simple graph"
    pass


@Aspect
def enforce_simple(slf, a, b, *args, **kwargs):
    # if Edge(a, b) in slf.edges:
    if list(filter(lambda other: (Node(a) == other.a and Node(b) == other.b) or (Node(a) == other.b and Node(b) == other.a), slf.edges)):
        raise RepeatedEdgeError("Edge already exists in simple graph")
    else:
        yield Proceed(slf, a, b, *args, **kwargs)


class TestGraphRefinement:
    def refine_test_cycle(self, original):
        def test_cycle(slf, graph):
            with pytest.raises(RepeatedEdgeError):
                graph.add("a", "b")
                graph.add("b", "a")

        return test_cycle


def select(composer):
    from basicGraph import Graph, Edge
    from basicGraph.test_graph import TestGraph

    weave(Graph, enforce_simple, methods="add")
    composer.compose(TestGraphRefinement(), TestGraph)
