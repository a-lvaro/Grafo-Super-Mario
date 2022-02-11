from cmath import inf


class Vertice:
    def __init__(self, vertice) -> None:
        self.profundidade = inf
        self.vertice = vertice
        self.aresta = []
        self.pai = inf

    def addAresta(self, u: int, v: int):
        if u == self.vertice:
            self.aresta.append(v)

        else:
            self.aresta.append(u)
            print('teste')
