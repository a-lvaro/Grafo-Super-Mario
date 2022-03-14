from cmath import inf


class Prim:
    def __init__(self, vertices: list, posicao: int) -> None:
        self.posicao = posicao
        queue = inf

        vertices[posicao].setPai(-1)
        queue = vertices[posicao].getAresta()

        while queue:
            queue = vertices[posicao].getAresta()

            if vertices[posicao].getPai() in queue:
                queue.remove(vertices[posicao].getPai())

            if len(queue) != 0:
                queue = max(queue) - 1
                vertices[posicao].setFilho(queue + 1)
                vertices[queue].setPai(posicao + 1)
                posicao = queue

        self.mostrar(vertices)

    def mostrar(self, vertices: list):

        posicao = self.posicao
        while posicao:
            print(posicao + 1)
            if vertices[posicao].getFilho() != inf:
                posicao = vertices[posicao].getFilho() - 1

            else:
                posicao = 0
