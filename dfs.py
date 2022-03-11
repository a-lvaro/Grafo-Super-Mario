from cmath import inf


class Dfs:
    def __init__(self, grafo: object, verticeInicio: int) -> None:
        self.cont = 0
        grafo.resetGrafo()
        self.cont += 1
        grafo.setProfundidade(verticeInicio, self.cont, 'ida')

        self.dfsNext(grafo, grafo.vertices[verticeInicio-1].getVertice())

        for vertice in grafo.vertices:
            if grafo.getProfundidade(verticeInicio) == inf:
                self.dfsNext(grafo, vertice.vertice)

    def dfsNext(self, grafo: object, vertice: int) -> None:
        for verticeAdj in grafo.getAdjacentes(vertice):
            if grafo.getProfundidade(verticeAdj) == inf:
                self.cont += 1
                grafo.setProfundidade(verticeAdj, self.cont, 'ida')
                self.dfsNext(grafo, verticeAdj)

        self.cont += 1
        grafo.setProfundidade(vertice, self.cont, 'volta')

    def mostrar(self):
        for vertice in self.vertices:
            print('Ida/Volta do Vertice', vertice.getProfundidade())
