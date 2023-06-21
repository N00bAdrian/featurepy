from featurepy import Composer
from basicGraph import Node
from copy import deepcopy


def has_cycle_path(graph, traversed_nodes: list[Node], dest_node: Node):

    if dest_node in traversed_nodes:
        return True

    for node, edge in dest_node.neighbours:
        if edge in graph.edges:
            new_graph = deepcopy(graph)
            new_graph.edges.remove(edge)
            if has_cycle_path(new_graph, [dest_node] + traversed_nodes, node):
                return True

    return False


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
