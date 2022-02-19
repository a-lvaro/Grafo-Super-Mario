from cmath import inf
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
            print('Profundidade do Vertice ',
                  vertice.vertice, ': ', vertice.profundidade)

    def mostrarPai(self):
        for vertice in self.vertices:
            print(vertice.vertice, 'pai: ', vertice.pai)

    def mostraIdaVolta(self):
        for vertice in self.vertices:
            print('Ida/Volta do Vertice', vertice.vertice,
                  ': ', vertice.ida, '/', vertice.volta)

    '''--------------------------------------------------------
        como a lista começa em 0 e os vértices em 1,
        para achar a localização dos vértices na lista será n - 1
        -------------------------------------------------------'''

    def setProfundidade(self, vertice: int, profundidade: int) -> None:
        self.vertices[vertice - 1].profundidade = profundidade

    def setIda(self, vertice: int, cont: int) -> int:
        cont += 1
        self.vertices[vertice - 1].ida = cont
        return cont

    def setVolta(self, vertice: int, cont: int) -> None:
        cont = cont + 1
        self.vertices[vertice - 1].volta = cont
        return cont

    def getProfundidade(self, vertice: int) -> int:
        return self.vertices[vertice - 1].profundidade

    def getAdjacentes(self, vertice: int) -> list:
        return self.vertices[vertice - 1].aresta

    def setPai(self, vertice: int, pai: int) -> None:
        self.vertices[vertice - 1].pai = pai

    def getPai(self, vertice: int) -> int:
        return self.vertices[vertice - 1].pai

    def getIda(self, vertice: int) -> int:
        return self.vertices[vertice - 1].ida

    def getVolta(self, vertice: int) -> int:
        return self.vertices[vertice - 1].volta

    def getVertice(self, vertice: int) -> int:
        return self.vertices[vertice - 1].vertice

    def resetGrafo(self):
        for vertice in range(self.qtdVertices):
            self.setProfundidade(vertice, inf)
            self.setPai(vertice, inf)
            self.setIda(vertice, inf)
            self.setVolta(vertice, inf)
