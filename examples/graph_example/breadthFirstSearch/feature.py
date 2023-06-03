from featurepy import Composer


class GraphRefinementTree:
    def introduce_search_from(self):
        def search_from(slf, a):
            result = [a]
            prev_result = []
            while set(prev_result) != set(result):
                prev_result = result
                result = []
                for x in prev_result:
                    result += slf.nodes_from(x) + [x]
                result = list(set(result))
                print(f"prev: {prev_result} res: {result}")

            return result

        return search_from


class TestGraphRefinementTree:
    def introduce_test_search_from(self):
        def test_search_from(slf, new_graph):
            new_graph.add("a", "b")
            new_graph.add("a", "c")

            assert set(new_graph.search_from("a")) == set(
                new_graph.nodes_from("a") + ["a"])

            new_graph.add("b", "d")
            new_graph.add("e", "c")

            new_graph.add("x", "y")
            new_graph.add("y", "z")

            assert set(new_graph.search_from("a")) == set(new_graph.nodes_from(
                "a") + new_graph.nodes_from("b") + new_graph.nodes_from("c") + ["a"])
            assert set(new_graph.search_from("b")) == set(
                new_graph.nodes_from("b") + new_graph.nodes_from("a") + new_graph.nodes_from("c") + ["b"])
            assert set(new_graph.search_from("x")) == set(
                new_graph.nodes_from("x") + new_graph.nodes_from("y") + ["x"])

        return test_search_from


def select(composer: Composer):
    from basicGraph import Graph
    from fixtures import TestGraph
    composer.compose(GraphRefinementTree(), Graph)
    composer.compose(TestGraphRefinementTree(), TestGraph)
