from featurepy import Composer, Aspect, weave, Proceed
from basicGraph import Edge


class WeightedEdgeRefinement:
    def refine___init__(self, original):
        def __init__(slf, *args, weight=1, **kwargs):
            original(slf, *args, **kwargs)
            slf.weight = weight

        return __init__

    def refine___eq__(self, original):
        def __eq__(slf, other):
            return original(slf, other) and slf.weight == other.weight
        return __eq__

    def refine___le__(self, original):
        def __le__(self, other):
            if not isinstance(other, Edge):
                raise Exception("Edges must be compared to other Edges")
            return self.weight <= other.weight
        return __le__

    def refine___lt__(self, original):
        def __lt__(self, other):
            if not isinstance(other, Edge):
                raise Exception("Edges must be compared to other Edges")
            return self.weight < other.weight
        return __lt__

    def refine___ge__(self, original):
        def __ge__(self, other):
            if not isinstance(other, Edge):
                raise Exception("Edges must be compared to other Edges")
            return self.weight >= other.weight
        return __ge__

    def refine___gt__(self, original):
        def __gt__(self, other):
            if not isinstance(other, Edge):
                raise Exception("Edges must be compared to other Edges")
            return self.weight > other.weight
        return __gt__


def add_weight_aspect(weight):
    @Aspect
    def add_weight(*args, **kwargs):
        kwargs['weight'] = weight
        yield Proceed(*args, **kwargs)

    return add_weight


class GraphRefinement:
    def refine_add(self, original):
        def add(slf, a, b, *args, weight=1, **kwargs):
            with weave(Edge, add_weight_aspect(weight), methods="__init__"):
                return original(slf, a, b, *args, **kwargs)

        return add


class TestEdgeRefinement:
    def introduce_test_weights(self):
        def test_weights(slf):
            assert Edge("a", "b").weight == 1
            assert Edge("a", "b", weight=2).weight == 2
            assert Edge(1, 2) != Edge(1, 2, weight=2)

        return test_weights

    def introduce_test_edge_comparison(self):
        def test_edge_comparison(slf):
            e1 = Edge(1, 2)
            e2 = Edge(3, 4, weight=2)

            assert e1 <= e2
            assert e1 < e2
            assert e2 >= e1
            assert e2 > e1

            assert e1 != e2

        return test_edge_comparison


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
    composer.compose(GraphRefinement(), Graph)
    composer.compose(TestEdgeRefinement(), TestEdge)
    composer.compose(TestGraphRefinement(), TestGraph)
