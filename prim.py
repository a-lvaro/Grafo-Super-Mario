from cmath import inf


class Prim:
    def __init__(self, vertices: list, posicao: int) -> None:
        self.posicao = posicao

        aux = posicao
        vertices[posicao].setPai(-1)
        queue = vertices[posicao].getAresta()
        queue = max(queue)
        vertices[posicao].setFilho(queue)
        queue -= 1

        while queue:
            vertices[queue].setPai(aux + 1)
            aux = queue
            queue = vertices[queue].getAresta()

            if vertices[aux].getPai() in queue:
                queue.remove(vertices[aux].getPai())

            if len(queue) != 0:
                queue = max(queue)
                vertices[aux].setFilho(queue)
                queue -= 1

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
