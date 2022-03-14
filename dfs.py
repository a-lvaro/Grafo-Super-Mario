from cmath import inf


class Dfs:
    def __init__(self, vertices: list, posicao: int) -> None:
        self.cont = 1

        vertices[posicao].setProfundidade(self.cont, 'ida')

        self.dfsNext(vertices, vertices[posicao].getVertice() - 1)

        for vertice in vertices:
            if vertices[posicao].getProfundidade() == inf:
                self.dfsNext(vertices, vertice.getVertice() - 1)

        self.mostrar(vertices)

    def dfsNext(self, vertices: list, posicao: int) -> None:

        for verticeAdj in vertices[posicao].getAresta():
            verticeAdj -= 1
            if vertices[verticeAdj].getProfundidade() == inf:
                self.cont += 1
                vertices[verticeAdj].setProfundidade(self.cont, 'ida')
                self.dfsNext(vertices, verticeAdj)

        self.cont += 1
        vertices[posicao].setProfundidade(self.cont, 'volta')

    def mostrar(self, vertices: list):

        print('\n\nDFS: busca em profundidade: \n')
        for vertice in vertices:
            print('Ida/Volta do Vertice {} : {}'.format(vertice.getVertice(),
                  vertice.getProfundidade()))
