import pytest
from basicGraph import Edge, Node


class RepeatedEdgeError(Exception):
    "Edge already exists in simple graph"
    pass


# class SimpleEdgeRefinement:
#     def refine___eq__(self, original):
#         def __eq__(cls, other):
#             if isinstance(other, Edge):
#                 return (cls.a == other.a and cls.b == other.b) or (cls.a == other.b and cls.b == other.a)
#             return False

#         return __eq__


class SimpleGraphRefinement:
    def refine_add(self, original):
        def add(cls, *args, **kwargs):
            if Edge(*args, **kwargs) in cls.edges:
                raise RepeatedEdgeError
            else:
                original(cls, *args, **kwargs)
        return add


class TestRefinement:
    def refine_test_cycle(self, original):
        def test_cycle(slf, new_graph):
            with pytest.raises(RepeatedEdgeError):
                new_graph.add("a", "b")
                new_graph.add("b", "a")

        return test_cycle


def select(composer):
    from basicGraph import Graph
    from fixtures import TestGraph

    composer.compose(SimpleGraphRefinement(), Graph)
    composer.compose(TestRefinement(), TestGraph)
