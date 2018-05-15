import Vertice

class Grafo:
    def __init__(self):
        self.vertices = {}

    def addVertice(self, vertice):
        self.vertices[vertice.id] = vertice.list

    def addAresta(self, verticeA, verticeB):
        verticeA.addVert(verticeB)
        self.vertices[verticeA.id] = verticeA.list
        self.vertices[verticeB.id] = verticeB.list

    def adjacencyList(self):
        if len(self.vertices) >= 1:
            return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]
        else:
            return dict()
