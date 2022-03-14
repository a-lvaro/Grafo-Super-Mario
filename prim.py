from cmath import inf


class Prim:
    def __init__(self, vertices: list, posicao: int) -> None:
        self.posicao = posicao
        fila = inf

        vertices[posicao].setPai(-1)

        while fila:
            fila = vertices[posicao].getAresta()

            if vertices[posicao].getPai() in fila:
                fila.remove(vertices[posicao].getPai())

            if len(fila) != 0:
                fila = max(fila)
                vertices[posicao].setFilho(fila)
                vertices[fila - 1].setPai(posicao + 1)
                posicao = fila - 1

        self.mostrar(vertices)

    def mostrar(self, vertices: list):

        posicao = self.posicao
        while posicao:
            print(vertices[posicao].getVertice())

            if vertices[posicao].getFilho() != inf:
                posicao = vertices[posicao].getFilho() - 1

            else:
                posicao = 0
