from featuremonkey import select
from basicGraph import *

select('weightedGraph', 'simpleGraph', 'basicGraph')

g = Graph()
g.add(Node("a"), Node("b"))
g.add(Node("b"), Node("a"), weight=5)
g.add(Node("b"), Node("c"))
print(g)