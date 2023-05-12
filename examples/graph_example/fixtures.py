import pytest

@pytest.fixture
def new_graph():
    g = Graph()
    g.nodes = []
    g.edges = []
    return g