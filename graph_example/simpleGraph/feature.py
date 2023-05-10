from basicGraph import Edge

class RepeatedEdgeError(Exception):
    "Edge already exists in simple graph"
    pass

class SimpleEdgeRefinement:
    def refine___eq__(self, original):
        def __eq__(cls, other):
            if isinstance(other, Edge):
                return (cls.a == other.a and cls.b == other.b) or (cls.a == other.b and cls.b == other.a)
            return False

        return __eq__

class SimpleGraphRefinement:
    def refine_add(self, original):
        def add(cls, *args, **kwargs):
            if Edge(*args, **kwargs) in cls.edges:
                # print("Edge already exists in simple graph, skipping...")
                raise RepeatedEdgeError
            else:
                original(cls, *args, **kwargs)
        return add 


def select(composer):
    from basicGraph import Edge, Graph
    import basicGraph
    composer.compose(SimpleEdgeRefinement(), Edge)
    composer.compose(SimpleGraphRefinement(), Graph)