from featurepy import Composer
from basicGraph import Node


class GraphRefinement:
    def introduce__has_cycle_path(self):
        def _has_cycle_path(slf, traversed_nodes: list[Node], dest_node: Node):

            return dest_node in traversed_nodes or any([slf._has_cycle_path(traversed_nodes + [dest_node], d) for d in dest_node.neighbour_nodes()])

        return _has_cycle_path

    def introduce_has_cycle(self):
        def has_cycle(slf):
            return any([slf._has_cycle_path([], node) for node in slf.nodes])

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
