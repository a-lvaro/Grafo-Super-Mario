from numpy import loadtxt, int8


class MapaMario:
    # tirar as arestas da matriz e colocar em lista
    def __init__(self, vertices: list):

        with open('matriz.csv') as file:
            matrizMapa = loadtxt(file, delimiter=',', dtype=int8)

        for i in range(96):
            for j in range(96):
                if matrizMapa[i][j] == 1:
                    vertices[i].setAresta(j + 1, matrizMapa[i][j])
