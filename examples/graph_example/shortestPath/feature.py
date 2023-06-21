from featurepy import Composer
import numpy as np


class GraphRefinement:
    def introduce__to_adj_matrix(self):
        def _to_adj_matrix(slf):
            n = len(slf.nodes)
            matrix = np.full((n, n), np.inf)
            np.fill_diagonal(matrix, 0)

            for edge in slf.edges:
                na = edge.a
                nb = edge.b
                w = edge.weight

                matrix[slf.nodes.index(na), slf.nodes.index(nb)] = min(
                    edge.weight, matrix[slf.nodes.index(na), slf.nodes.index(nb)])

            return matrix
        return _to_adj_matrix

    def introduce_shortest_paths(self):
        def shortest_paths(slf):
            n = len(slf.nodes)
            matrix = slf._to_adj_matrix()

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        matrix[i, j] = min(
                            matrix[i, j], matrix[i, k] + matrix[k, j])

            result = {}
            for i in range(n):
                for j in range(n):
                    a = slf.nodes[i].val
                    b = slf.nodes[j].val
                    w = matrix[i, j]
                    if w < np.inf and w > 0:
                        result[a, b] = w

            return result
        return shortest_paths


class TestGraphRefinement:
    def introduce_test_shortest_paths(self):
        def test_shortest_paths(slf, graph):
            graph.add(1, 2, weight=3)
            graph.add(1, 4, weight=5)
            graph.add(4, 3, weight=2)
            graph.add(3, 2, weight=1)
            graph.add(2, 4, weight=4)

            assert graph.shortest_paths() == {
                (1, 2): 3,
                (1, 3): 7,
                (1, 4): 5,
                (2, 3): 6,
                (2, 4): 4,
                (3, 2): 1,
                (3, 4): 5,
                (4, 2): 3,
                (4, 3): 2
            }
        return test_shortest_paths


def select(composer):
    from basicGraph import Graph
    from basicGraph.test_graph import TestGraph

    composer.compose(GraphRefinement(), Graph)
    composer.compose(TestGraphRefinement(), TestGraph)
