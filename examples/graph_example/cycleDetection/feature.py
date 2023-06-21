from featurepy import Composer
from basicGraph import Node
from copy import deepcopy


def has_cycle_path(graph, traversed_nodes: list[Node], dest_node: Node):

    # return dest_node in traversed_nodes or any([has_cycle_path(graph, traversed_nodes + [dest_node], d) for d in dest_node.neighbour_nodes()])
    for node, edge in dest_node.neighbours:
        if matching_edge_l := filter(lambda other: edge.a == other.a and edge.b == other.b, graph.edges):
            new_graph = deepcopy(graph)


class GraphRefinement:
    def introduce_has_cycle(self):
        def has_cycle(slf):
            return any([has_cycle_path(slf, [], node) for node in slf.nodes])

        return has_cycle


class TestGraphRefinement:
    def introduce_test_has_cycle(self):
        def test_has_cycle(slf, graph):
            assert not graph.has_cycle()

            graph.add("a", "b")
            assert not graph.has_cycle()

            graph.add("b", "c")
            assert not graph.has_cycle()

            graph.add("a", "c")
            assert not graph.has_cycle()

            graph.add("x", "y")
            graph.add("y", "z")
            graph.add("z", "x")
            assert graph.has_cycle()

        return test_has_cycle


def select(composer: Composer):
    from basicGraph import Graph
    from basicGraph.test_graph import TestGraph
    composer.compose(GraphRefinement(), Graph)
    composer.compose(TestGraphRefinement(), TestGraph)
