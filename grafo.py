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

        self.vertices = [Vertice(i + 1) for i in range(self.qtdVertices)]

        MapaMario(self.vertices)

    def bfs(self, verticeInicio: int):
        self.__resetGrafo()
        Bfs(self.vertices, verticeInicio - 1)

    def dfs(self, verticeInicio: int):
        self.__resetGrafo()
        Dfs(self.vertices, verticeInicio - 1)

    def topologia(self, verticeInicio: int):
        self.__resetGrafo()
        Topologica(self.vertices, verticeInicio - 1)

    def prim(self, verticeInicio: int):
        self.__resetGrafo()
        Prim(self.vertices, verticeInicio - 1)

    def __resetGrafo(self):
        for posicao in range(self.qtdVertices):
            self.vertices[posicao].setProfundidade(inf)
            self.vertices[posicao].setPai(inf)
            self.vertices[posicao].setFilho(inf)
