from featurepy import Composer


class GraphRefinement:
    def introduce__has_cycle_path(self):
        def _has_cycle_path(slf, traversed_nodes, dest_node):

            return (slf.nodes_from(dest_node) != []) and (dest_node in traversed_nodes or any([slf._has_cycle_path(traversed_nodes + [dest_node], d) for d in slf.nodes_from(dest_node)]))

        return _has_cycle_path

    def introduce_has_cycle(self):
        def has_cycle(slf):
            return any([slf._has_cycle_path([], node.val) for node in slf.nodes])

        return has_cycle


class TestGraphRefinement:
    def introduce_test_has_cycle(self):
        def test_has_cycle(slf, new_graph):
            assert not new_graph.has_cycle()

            new_graph.add("a", "b")
            assert not new_graph.has_cycle()

            new_graph.add("b", "c")
            assert not new_graph.has_cycle()

            new_graph.add("a", "c")
            assert not new_graph.has_cycle()

            new_graph.add("x", "y")
            new_graph.add("y", "z")
            new_graph.add("z", "x")
            assert new_graph.has_cycle()

        return test_has_cycle


def select(composer: Composer):
    from basicGraph import Graph
    from fixtures import TestGraph
    composer.compose(GraphRefinement(), Graph)
    composer.compose(TestGraphRefinement(), TestGraph)
