from cmath import inf


class Bfs:
    def __init__(self, vertices: list, posicao: int) -> None:
        aux = []

        vertices[posicao].setProfundidade(0)
        aux.append(posicao)

        while aux:
            u = aux.pop(0)

            for aresta in vertices[u].getAresta():
                aresta -= 1
                if vertices[aresta].getProfundidade() == inf:
                    aux.append(aresta)
                    vertices[aresta].setProfundidade(vertices[u].getProfundidade() + 1)

        self.mostrar(vertices)

    def mostrar(self, vertices: list) -> None:
        for vertice in vertices:
            print('Profundidade do Vertice ',
                  vertice.getVertice(), ': ', vertice.getProfundidade())
