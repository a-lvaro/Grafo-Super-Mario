from cmath import inf
from numpy import array, unique, amax, min, argwhere, delete
from sympy import inverse_laplace_transform


class Prim:
    def __init__(self, vertices: list, posicao: int) -> None:
        self.posicao = posicao
        fila = inf

        vertices[posicao].setPai(-1)

        while fila:
            fila = array(vertices[posicao].getArestaPeso())

            if vertices[posicao].getPai() in fila:
                index = argwhere(vertices[posicao].getPai() == fila[:, 0])
                fila = delete(fila, index, 0)

            if len(fila) != 0:
                fila = self.conferirMenorPeso(fila)
                vertices[posicao].setFilho(fila)
                vertices[fila - 1].setPai(posicao + 1)
                posicao = fila - 1

        self.mostrar(vertices)

    def conferirMenorPeso(self, fila: list) -> int:

        if len(unique(fila[:, 1])) != 1:
            fila = fila[fila[:, 1] == min(fila[:, 1], axis=0)]
            return amax(fila[:, 0], axis=0)

        else:
            return amax(fila[:, 0], axis=0)

    def mostrar(self, vertices: list):

        print('\n\nPRIM: menor caminho do vértice 53 ao vértice 96 \n')

        posicao = self.posicao
        while posicao:
            print(vertices[posicao].getVertice())

            if vertices[posicao].getFilho() != inf:
                posicao = vertices[posicao].getFilho() - 1

            else:
                posicao = 0
