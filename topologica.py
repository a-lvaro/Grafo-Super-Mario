from dfs import Dfs
from numpy import array


class Topologica:
    def __init__(self, grafo: object, verticeInicial: int) -> list:
        self.listaVoltas = []
        self.listaVertices = []

        Dfs(grafo, verticeInicial)

        for vertice in grafo.vertices:
            self.listaVoltas.append([vertice.getVertice(), grafo.getProfundidade(
                vertice.getVertice(), 'volta')])

        self.listaVoltas = array(self.listaVoltas)
        self.listaVoltas = self.listaVoltas[self.listaVoltas[:, 1].argsort(kind='quicksort'
                                                                           )][::-1]

    def mostrar(self) -> None:
        print('\nLista de vertices pela Ordenação Topológica: \n',
              self.listaVoltas)
