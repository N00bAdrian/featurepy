from featurepy import Composer
from basicGraph import Node


class SearchTypeError(Exception):
    "Unrecognized search type, please check that the search type is either BFS (breadth first search) or DFS (depth first search)"


def _depth_first_search(start: Node, traversed_nodes: list[Node]) -> list[Node]:
    traversed_nodes.append(start)
    for node in start.neighbour_nodes():
        if node not in traversed_nodes:
            traversed_nodes = _depth_first_search(node, traversed_nodes)
    return traversed_nodes


def _breadth_first_seach(start: Node) -> list[Node]:
    traversed_nodes = [start]
    queue = [start]
    while queue != []:
        x = queue.pop(0)
        for y in x.neighbour_nodes():
            if y not in traversed_nodes:
                traversed_nodes.append(y)
                queue.append(y)
    return traversed_nodes


class GraphRefinementTree:
    def __init__(self, type):
        self.type = type

    def introduce_search_from(self):
        def search_from(slf, start_val: any):
            start_node = slf.get_node(start_val)
            if self.type == "DFS":
                return _depth_first_search(start_node, [])
            elif self.type == "BFS":
                return _breadth_first_seach(start_node)
            else:
                raise SearchTypeError

        return search_from


class TestGraphRefinementTree:
    def introduce_test_search_from(self):
        def test_search_from(slf, graph):
            graph.add("a", "b")
            graph.add("a", "c")

            assert set(graph.search_from("a")) == set(graph.nodes)

            graph.add("b", "d")
            graph.add("c", "e")

            assert set(graph.search_from("a")) == set(graph.nodes)

            graph.add("x", "y")
            graph.add("y", "z")

            assert set(graph.search_from("a")) == set(
                [Node("a"), Node("b"), Node("c"), Node("d"), Node("e")])
            assert set(graph.search_from("x")) == set(
                [Node("x"), Node("y"), Node("z")])

        return test_search_from


def select(composer: Composer, type):
    from basicGraph import Graph
    from basicGraph.test_graph import TestGraph
    composer.compose(GraphRefinementTree(type), Graph)
    composer.compose(TestGraphRefinementTree(), TestGraph)
