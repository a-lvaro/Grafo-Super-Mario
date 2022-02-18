from cmath import inf


class Dfs:
    def __init__(self, g: object, t: object) -> None:
        g.resetVertices()
        self.grafo = g
        self.cont = 1
        t.ida = self.cont

        self.dfsNext(t)
        for vertice in self.grafo.vertices:
            if vertice.ida == inf:
                self.dfsNext(vertice)

        for vertice in self.grafo.vertices:
            print("Valores vertice", vertice.vertice,
                  ": ", vertice.ida, "/", vertice.volta)

    def dfsNext(self, v: object):
        for vertice in v.aresta:
            if self.grafo.getIda(vertice) == inf:
                self.cont = self.cont + 1
                self.grafo.setIda(vertice, self.cont)
                self.dfsNext(self.grafo.vertices[vertice-1])
        self.cont = self.cont + 1
        v.volta = self.cont
