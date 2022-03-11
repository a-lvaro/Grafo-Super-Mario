from cmath import inf
from vertice import Vertice
from mapaMario import mapaMario


class Grafo:
    def __init__(self):
        self.vertices = []
        self.qtdVertices = 96

        for i in range(96):
            self.vertices.append(Vertice(i + 1))

        mapaMario(self.vertices)

    def mostrarArestas(self):
        for vertice in self.vertices:
            print(vertice.getAresta())

    def mostrarProfundidade(self):
        for vertice in self.vertices:
            print('Profundidade do Vertice ',
                  vertice.getVertice(), ': ', vertice.getProfundidade())

    def mostraIdaVolta(self):
        for vertice in self.vertices:
            print('Ida/Volta do Vertice', vertice.getProfundidade())

    '''--------------------------------------------------------
        como a lista começa em 0 e os vértices em 1,
        para achar a localização dos vértices na lista será n - 1
        -------------------------------------------------------'''

    def setProfundidadeDFS(self, vertice: int, cont: int, flag: str) -> int:
        cont += 1

        if flag == 'ida':
            self.vertices[vertice - 1].profundidade = [cont, inf]

        if flag == 'volta':
            self.vertices[vertice - 1].profundidade[1] = cont

        return cont

    def getProfundidadeDFS(self, vertice: int, flag: str) -> int:
        if flag == 'volta':
            return self.vertices[vertice - 1].profundidade[1]

    def setProfundidade(self, vertice: int, profundidade: int) -> None:
        self.vertices[vertice - 1].setProfundidade(profundidade)

    def getProfundidade(self, vertice: int) -> int:
        return self.vertices[vertice - 1].getProfundidade()

    def getAdjacentes(self, vertice: int) -> list:
        return self.vertices[vertice - 1].getAresta()

    def getVertice(self, vertice: int) -> int:
        return self.vertices[vertice - 1].getVertice()

    def resetGrafo(self):
        for vertice in range(self.qtdVertices):
            self.setProfundidade(vertice, inf)
