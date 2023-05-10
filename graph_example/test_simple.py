from featuremonkey import select
import pytest

# select("simpleGraph", "basicGraph")
# from basicGraph import *
# from simpleGraph import RepeatedEdgeError

# @pytest.fixture
# def new_graph():
#     g = Graph()
#     g.nodes = []
#     g.edges = []
#     return g

# class TestSimpleGraph:
#     def test_error(self, new_graph):
#         with pytest.raises(RepeatedEdgeError):
#             new_graph.add(Node("a"), Node("b"))
#             new_graph.add(Node("b"), Node("a"))