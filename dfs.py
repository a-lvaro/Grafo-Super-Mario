from cmath import inf


class Dfs:
    def __init__(self, grafo: object, verticeInicio: int) -> None:
        self.cont = 0
        grafo.resetGrafo()

        self.cont = grafo.setProfundidadeDFS(verticeInicio, self.cont, 'ida')

        self.dfsNext(grafo, grafo.vertices[verticeInicio-1].getVertice())

        for vertice in grafo.vertices:
            if grafo.getProfundidade(verticeInicio) == inf:
                self.dfsNext(grafo, vertice.vertice)

    def dfsNext(self, grafo: object, vertice: int) -> None:
        for verticeAdj in grafo.getAdjacentes(vertice):
            if grafo.getProfundidade(verticeAdj) == inf:
                self.cont = grafo.setProfundidadeDFS(
                    verticeAdj, self.cont, 'ida')
                self.dfsNext(grafo, verticeAdj)

        self.cont = grafo.setProfundidadeDFS(vertice, self.cont, 'volta')
