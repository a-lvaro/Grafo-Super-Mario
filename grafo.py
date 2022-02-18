from vertice import Vertice
from numpy import loadtxt, int8


class Grafo:
    def __init__(self):
        self.vertices = []
        self.qtdVertices = 96

        for i in range(96):
            self.vertices.append(Vertice(i + 1))

        self.createMario()

    # tirar as arestas da matriz e colocar em lista
    def createMario(self):
        file = open('matriz.csv')
        matrizMapa = loadtxt(file, delimiter=',', dtype=int8)

        for i in range(96):
            for j in range(96):
                if matrizMapa[i][j] == 1:
                    self.vertices[i].setAresta(j + 1)

    def mostrarArestas(self):
        for vertice in self.vertices:
            print(vertice.aresta)

    def mostrarProfundidade(self):
        for vertice in self.vertices:
            print(vertice.vertice, 'profundidade: ', vertice.profundidade)

    def mostrarPai(self):
        for vertice in self.vertices:
            print(vertice.vertice, 'pai: ', vertice.pai)

    '''--------------------------------------------------------
        como a lista começa em 0 e os vértices em 1,
        para achar a localização dos vértices na lista será n - 1
        -------------------------------------------------------'''

    def setProfundidade(self, vertice: int, profundidade: int) -> None:
        self.vertices[vertice - 1].profundidade = profundidade

    def getProfundidade(self, vertice: int) -> int:
        return self.vertices[vertice - 1].profundidade

    def getAdjacentes(self, vertice: int) -> list:
        return self.vertices[vertice - 1].aresta

    def setPai(self, vertice: int, pai: int) -> None:
        self.vertices[vertice - 1].pai = pai

    def getPai(self, vertice: int) -> int:
        return self.vertices[vertice - 1].pai
