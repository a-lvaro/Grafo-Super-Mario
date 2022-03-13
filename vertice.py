from cmath import inf


class Vertice:
    def __init__(self, vertice) -> None:
        self.__profundidade = inf
        self.__vertice = vertice
        self.__aresta = []
        self.pai = inf
        self.filho = inf

    def setPai(self, pai: int) -> None:
        self.pai = pai

    def getPai(self) -> int:    
        return self.pai

    def setFilho(self, filho: int) -> None:
        self.filho = filho

    def getFilho(self) -> int:    
        return self.filho


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
            self.__profundidade[0] = profundidade

        if flag == 'volta':
            self.__profundidade[1] = profundidade

    def getProfundidade(self, flag='default') -> int:
        if flag == 'default':
            return self.__profundidade

        if flag == 'volta':
            return self.__profundidade[1]
