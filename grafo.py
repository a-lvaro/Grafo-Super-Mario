from cmath import inf
from vertice import Vertice
from mapaMario import MapaMario
from bfs import Bfs
from dfs import Dfs
from topologica import Topologica
from prim import Prim


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

    def bfs(self, verticeInicio: int):
        # self.resetGrafo()
        Bfs(self.vertices, verticeInicio - 1)

    def dfs(self, verticeInicio: int):
        # self.resetGrafo()
        Dfs(self.vertices, verticeInicio - 1)

    def topologia(self, verticeInicio: int):
        # self.resetGrafo()
        Topologica(self.vertices, verticeInicio - 1)

    def prim(self, verticeInicio: int):
        Prim(self.vertices, verticeInicio - 1)

    def mostraIdaVolta(self):
        for vertice in self.vertices:
            print('Ida/Volta do Vertice {} : {}'.format(vertice.getVertice(),
                  vertice.getProfundidade()))

    '''--------------------------------------------------------
        como a lista começa em 0 e os vértices em 1,
        para achar a localização dos vértices na lista será n - 1
        -------------------------------------------------------'''

    def resetGrafo(self):
        for vertice in range(self.qtdVertices):
            self.setProfundidade(vertice, inf)
