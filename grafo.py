from cmath import inf
from vertice import Vertice
from mapaMario import MapaMario


class Grafo:
    def __init__(self):
        self.vertices = []
        self.qtdVertices = 96

        for i in range(self.qtdVertices):
            self.vertices.append(Vertice(i + 1))

        MapaMario(self.vertices)

    def getQtdVertices(self) -> int:
        return self.qtdVertices

    def mostrarArestas(self):
        for vertice in self.vertices:
            print(vertice.getAresta())

    def mostrarProfundidade(self):
        for vertice in self.vertices:
            print('Profundidade do Vertice ',
                  vertice.getVertice(), ': ', vertice.getProfundidade())

    '''--------------------------------------------------------
        como a lista começa em 0 e os vértices em 1,
        para achar a localização dos vértices na lista será n - 1
        -------------------------------------------------------'''

    def setProfundidade(self, vertice: int, profundidade: int, flag='default') -> None:
        if flag == 'default':
            self.vertices[vertice - 1].setProfundidade(profundidade)

        # usado no dfs
        if flag == 'ida':
            self.vertices[vertice - 1].setProfundidade([profundidade, inf])

        if flag == 'volta':
            self.vertices[vertice - 1].setProfundidade(profundidade, 'volta')

    def getProfundidade(self, vertice: int, flag='default') -> int:
        if flag == 'default':
            return self.vertices[vertice - 1].getProfundidade()

        if flag == 'volta':
            return self.vertices[vertice - 1].getProfundidade('volta')

    def getAdjacentes(self, vertice: int) -> list:
        return self.vertices[vertice - 1].getAresta()

    def getVertice(self, vertice: int) -> int:
        return self.vertices[vertice - 1].getVertice()

    def resetGrafo(self):
        for vertice in range(self.qtdVertices):
            self.setProfundidade(vertice, inf)
