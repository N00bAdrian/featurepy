from featurepy import Composer
from cycleDetection.feature import has_cycle_path
from copy import deepcopy
from math import inf
import heapq

from basicGraph.graph import Graph, Edge, Node


class MSTTypeError(Exception):
    '''Raise when neither Prim nor Kruskal is passed as an argument'''


def _kruskal(edges: list[Edge]):
    heapq.heapify(edges)
    mst = Graph()
    while edges != []:
        e = heapq.heappop(edges)
        a = e.a.val
        b = e.b.val
        w = e.weight

        new_tree = deepcopy(mst)
        new_tree.add(a, b, weight=w)
        if not has_cycle_path(new_tree, [], e.a):
            mst = new_tree

    return mst


def _prim(nodes):
    mst = Graph()
    pqueue = [(0, None, nodes[0])] + [(inf, None, node) for node in nodes[1:]]
    while pqueue != []:
        _, e, n = heapq.heappop(pqueue)
        if e:
            a = e.a.val
            b = e.b.val
            w = e.weight
            mst.add(a, b, weight=w)
        else:
            mst.nodes.append(n)

        for node, edge in n.neighbours:
            if node not in mst.nodes:
                p, qe, qn = list(
                    filter(lambda tup, node=node: tup[2] == node, pqueue))[0]
                if edge.weight < p:
                    pqueue.remove((p, qe, qn))
                    heapq.heappush(pqueue, (edge.weight, edge, node))

    return mst


class GraphRefinement:
    def __init__(self, type: str):
        self.type = type

    def introduce_get_mst(self):
        if self.type == "prim":
            def get_mst(slf):
                return _prim(slf.nodes)
        elif self.type == "kruskal":
            def get_mst(slf):
                return _kruskal(slf.edges)
        else:
            raise MSTTypeError(
                "Unrecognized MST type, please check that the MST type is either prim or kruskal.")

        return get_mst


class TestGraphRefinement:
    def introduce_test_mst(self):
        def test_mst(slf, graph):
            graph.add(1, 2, weight=3)
            graph.add(2, 3, weight=4)
            graph.add(1, 3, weight=5)
            graph.add(1, 4, weight=4)
            graph.add(4, 3, weight=2)

            mst = Graph()
            mst.add(1, 2, weight=3)
            mst.add(1, 4, weight=4)
            mst.add(4, 3, weight=2)

            assert graph.get_mst() == mst

        return test_mst


def select(composer, type: str):
    from basicGraph import Graph
    from basicGraph.test_graph import TestGraph

    composer.compose(GraphRefinement(type), Graph)
    composer.compose(TestGraphRefinement(), TestGraph)
