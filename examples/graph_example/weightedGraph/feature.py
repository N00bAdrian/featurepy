from featurepy import Composer, Aspect, weave, Proceed
from basicGraph import Edge


class WeightedEdgeRefinement:
    def refine___init__(self, original):
        def __init__(slf, *args, weight=1, **kwargs):
            original(slf, *args, **kwargs)
            slf.weight = weight

        return __init__


def add_weight_aspect(weight):
    @Aspect
    def add_weight(*args, **kwargs):
        kwargs['weight'] = weight
        yield Proceed(*args, **kwargs)

    return add_weight


class TestEdgeRefinement:
    def introduce_test_weights(self):
        def test_weights(slf):
            assert Edge("a", "b").weight == 1
            assert Edge("a", "b", weight=2).weight == 2

        return test_weights


class TestGraphRefinement:
    def introduce_test_add_weighted_edge(self):
        def test_add_weighted_edge(slf, graph):
            graph.add("a", "b")
            graph.add("c", "d", weight=2)

            assert graph.edges[0].weight == 1
            assert graph.edges[1].weight == 2

        return test_add_weighted_edge


def select(composer: Composer):
    from basicGraph import Edge, Graph
    from basicGraph.test_graph import TestEdge, TestGraph

    composer.compose(WeightedEdgeRefinement(), Edge)
    Graph.register_aspect('add', Edge, add_weight_aspect)
    composer.compose(TestEdgeRefinement(), TestEdge)
    composer.compose(TestGraphRefinement(), TestGraph)
