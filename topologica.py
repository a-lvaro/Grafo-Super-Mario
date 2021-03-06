from dfs import Dfs
from numpy import array


class Topologica:
    def __init__(self, vertices: list, posicao: int) -> list:
        self.listaVoltas = []

        Dfs(vertices, posicao)

        for vertice in vertices:
            self.listaVoltas.append([vertice.getVertice(
            ), vertices[vertice.getVertice() - 1].getProfundidade('volta')])

        self.listaVoltas = array(self.listaVoltas)
        self.listaVoltas = self.listaVoltas[self.listaVoltas[:, 1].argsort(kind='quicksort'
                                                                           )][::-1]

        self.mostrar()

    def mostrar(self) -> None:
        print('\n\nLista de vertices pela Ordenação Topológica: \n')

        for vertice, profundidade in self.listaVoltas:
            print('Vértice     {}      :       Profundidade     {}'.format(
                vertice, profundidade))
