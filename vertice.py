from cmath import inf


class Vertice:
    def __init__(self, vertice) -> None:
        self.profundidade = inf
        self.__vertice = vertice
        self.__aresta = []

    def setAresta(self, u: int) -> None:
        self.__aresta.append(u)

    def getAresta(self) -> list:
        return self.__aresta

    def getVertice(self) -> int:
        return self.__vertice

    def setProfundidade(self, profundidade: int) -> None:
        self.profundidade = profundidade

    def getProfundidade(self) -> int:
        return self.profundidade
