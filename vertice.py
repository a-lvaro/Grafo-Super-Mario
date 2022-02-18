from cmath import inf


class Vertice:
    def __init__(self, vertice) -> None:
        self.profundidade = inf
        self.vertice = vertice
        self.aresta = []
        self.pai = inf

    def setAresta(self, u: int):
        self.aresta.append(u)

    def setProfundidade(self):
        pass
