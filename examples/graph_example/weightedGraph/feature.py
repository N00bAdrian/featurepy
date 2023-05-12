from featuremonkey import Composer
from basicGraph import Edge

class WeightedEdgeRefinement:
    def refine___init__(self, original):
        def __init__(cls, *args, weight=1, **kwargs):
            original(cls, *args, **kwargs)
            cls.weight = weight

        return __init__

    def refine___str__(self, original):
        def __str__(cls):
            return f"({original(cls)}, w={cls.weight})"
        
        return __str__

class WeightedGraphRefinement:
    def refine_add(self, original):
        def add(cls, *args, weight=1, **kwargs):
            cls.edges.append(Edge(*args, weight=weight, **kwargs))

        return add 


def select(composer:Composer):
    from basicGraph import Edge, Graph
    composer.compose(WeightedEdgeRefinement(), Edge)
    composer.compose(WeightedGraphRefinement(), Graph)
