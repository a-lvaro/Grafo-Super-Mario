from cmath import inf


class Dfs:
    def __init__(self, grafo: object, verticeInicio: int) -> None:
        self.cont = 0
        grafo.resetGrafoDfs()
        self.cont = grafo.setIda(verticeInicio, self.cont)

        self.dfsNext(grafo, grafo.vertices[verticeInicio-1].vertice)

        for vertice in grafo.vertices:
            if grafo.getIda(verticeInicio) == inf:
                self.dfsNext(grafo, vertice.vertice)

    def dfsNext(self, grafo: object, vertice: int) -> None:
        for verticeAdj in grafo.getAdjacentes(vertice):
            if grafo.getIda(verticeAdj) == inf:
                self.cont = grafo.setIda(verticeAdj, self.cont)
                self.dfsNext(grafo, verticeAdj)

        self.cont = grafo.setVolta(vertice, self.cont)
