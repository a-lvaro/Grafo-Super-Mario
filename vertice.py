from cmath import inf


class Vertice:
    def __init__(self, vertice) -> None:
        self.__profundidade = inf
        self.__vertice = vertice
        self.__aresta = []

    def setAresta(self, u: int) -> None:
        self.__aresta.append(u)

    def getAresta(self) -> list:
        return self.__aresta

    def getVertice(self) -> int:
        return self.__vertice

    def setProfundidade(self, profundidade: int, flag='default') -> None:
        if flag == 'default':
            self.__profundidade = profundidade

        # usado no dfs
        if flag == 'ida':
            self.__profundidade = [profundidade, inf]

        if flag == 'volta':
            self.__profundidade[1] = profundidade

    def getProfundidade(self, flag='default') -> int:
        if flag == 'default':
            return self.__profundidade

        if flag == 'volta':
            return self.__profundidade[1]
