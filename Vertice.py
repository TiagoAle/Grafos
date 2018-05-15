class Vertice:
    def __init__(self, vertice):
        self.id = vertice
        self.list = []

    def addVert(self, vert):
        if vert.id not in self.list:
            self.list.append(vert.id)
            vert.list.append(self.id)
            self.list = sorted(self.list)
            vert.list = sorted(vert.list)

    def getList(self):
        return str(self.list)