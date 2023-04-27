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
    
    def __str__(self):
        return f"{str(self.a)}-{str(self.b)}"

class Graph:
    edges = []

    def add(self, a:Node, b:Node):
        self.edges.append(Edge(a, b))
    
    def __str__(self):
        return ",".join([str(edge) for edge in self.edges])