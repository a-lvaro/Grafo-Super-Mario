from cmath import inf


class Prim:
    def __init__(self, vertices: list, posicao: int) -> None:
        self.posicao = posicao

        vertices[posicao].setPai(-1)
        queue = vertices[posicao].getAresta()
        queue = max(queue)
        queue -= 1
        vertices[posicao].setFilho(queue + 1)
        vertices[queue].setPai(posicao + 1)
        posicao = queue

        while queue:
            # vertices[posicao].setPai(aux + 1)
            queue = vertices[posicao].getAresta()

            if vertices[posicao].getPai() in queue:
                queue.remove(vertices[posicao].getPai())

            if len(queue) != 0:
                queue = max(queue)
                queue -= 1
                vertices[posicao].setFilho(queue + 1)
                vertices[queue].setPai(posicao + 1)
                posicao = queue

        self.mostrar(vertices)

    def mostrar(self, vertices: list):

        aux = self.posicao
        while aux:
            print(aux + 1)
            if vertices[aux].getFilho() != inf:
                aux = vertices[aux].getFilho()
                aux -= 1
            else:
                aux = 0
