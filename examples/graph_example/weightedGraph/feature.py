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


class WeightedGraphRefinement:
    def refine_add(self, original):
        def add(slf, *args, weight=1, **kwargs):
            with weave(Edge, add_weight_aspect(weight), methods='__init__'):
                original(slf, *args, **kwargs)

        return add


class TestEdgeRefinement:
    def introduce_test_weights(self):
        def test_weights(slf):
            assert Edge("a", "b").weight == 1
            assert Edge("a", "b", weight=2).weight == 2

        return test_weights


def select(composer: Composer):
    from basicGraph import Edge, Graph
    from basicGraph.test_graph import TestEdge

    composer.compose(WeightedEdgeRefinement(), Edge)
    composer.compose(WeightedGraphRefinement(), Graph)
    composer.compose(TestEdgeRefinement(), TestEdge)
