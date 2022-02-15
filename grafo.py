from vertice import Vertice

# teste
class Grafo:
    def __init__(self, vertices: int):
        self.vertices = []
        self.qtdVertices = vertices

        for i in range(vertices):
            self.vertices.append(Vertice(i + 1))

    def addAresta(self, u: int, v: int):
        # grafo não orientado, os dois vértices precisam saber que estão ligados
        if not v in self.vertices[u - 1].aresta:
            self.vertices[u - 1].addAresta(u, v)
            self.vertices[v - 1].addAresta(u, v)

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
