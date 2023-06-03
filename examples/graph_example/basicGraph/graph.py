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
    def __init__(self, a, b):
        self.a = Node(a)
        self.b = Node(b)

    def go_from(self, a):
        na = Node(a)
        if na == self.a:
            return self.b.val
        elif na == self.b:
            return self.a.val

        return None

    def __eq__(cls, other):
        if isinstance(other, Edge):
            return (cls.a == other.a and cls.b == other.b) or (cls.a == other.b and cls.b == other.a)
        return False

    def __str__(self):
        return f"{str(self.a)}-{str(self.b)}"

    def __repr__(self):
        return f"{str(self.a)}-{str(self.b)}"


class Graph:
    def __init__(self):
        self.edges = []
        self.nodes = []

    def nodes_from(self, a):
        result = []
        for edge in self.edges:
            if x := edge.go_from(a):
                result.append(x)

        return result

    def add(self, a, b):
        na = Node(a)
        nb = Node(b)
        if na not in self.nodes:
            self.nodes.append(na)

        if nb not in self.nodes:
            self.nodes.append(nb)

        self.edges.append(Edge(a, b))

    def __repr__(self):
        return ",".join([str(edge) for edge in self.edges])

    def __str__(self):
        return ",".join([str(edge) for edge in self.edges])
