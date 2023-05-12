class Node:
    def __init__(self, val):
        self.val = val
    
    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.val == other.val
        return False 
    
class Edge:
    def __init__(self, a: Node, b: Node):
        self.a = a
        self.b = b
    
    def __repr__(self):
        return f"{str(self.a)}-{str(self.b)}"
    
    def __str__(self):
        return f"{str(self.a)}-{str(self.b)}"

class Graph:
    edges = []
    nodes = []

    def add(self, a:Node, b:Node):
        if a not in self.nodes:
            self.nodes.append(a)

        if b not in self.nodes:
            self.nodes.append(b)

        self.edges.append(Edge(a, b))
    
    def __repr__(self):
        return ",".join([str(edge) for edge in self.edges])

    def __str__(self):
        return ",".join([str(edge) for edge in self.edges])