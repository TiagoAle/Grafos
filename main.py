from Vertice import Vertice
from Graph import Grafo
import graphviz as gv

def main():

    dot = gv.Graph(format='png')

    dot.node('A')
    dot.node('B')
    dot.node('C')
    dot.node('D')
    dot.node('E')

    dot.edge('A', 'B')
    dot.edge('A', 'C')
    dot.edge('A', 'E')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('C', 'E')
    dot.edge('D', 'E')

    print(dot.source)

    filename = dot.render(filename='img/g1')
    print(filename)

    a = Vertice('A')
    b = Vertice('B')
    c = Vertice('C')
    d = Vertice('D')
    e = Vertice('E')

    a.addVert(b)
    a.addVert(c)
    a.addVert(e)
    b.addVert(c)
    c.addVert(d)
    c.addVert(e)
    d.addVert(c)

    g = Grafo()
    print
    graph(g)
    print
    g.addVertice(a)
    g.addVertice(b)
    g.addVertice(c)
    g.addVertice(d)
    g.addVertice(e)
    g.addAresta(b, d)
    print
    print
    print(graph(g))

def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacencyList())

if __name__ == "__main__":
    main()
