from grafo import Grafo
from dfs import Dfs


class Topologica:
    def __init__(self) -> None:
        self.listaVoltas = []
        self.listaVertices = []

    def topologica(self, grafo: object, verticeInicial: int) -> list:
        dfs = Dfs(grafo, verticeInicial)

        for vertice in grafo.vertices:
            self.listaVoltas.append(grafo.getVolta(vertice.vertice))

        self.listaVoltas.sort(reverse=True)

        for volta in range(len(self.listaVoltas)):
            for vertice in grafo.vertices:
                if grafo.getVolta(vertice.vertice) == self.listaVoltas[volta]:
                    self.listaVertices.append(vertice.vertice)
                    print('Vertice: ', vertice.vertice,
                          ' - Valor de Volta: ', self.listaVoltas[volta])

        return self.listaVertices
