from cmath import inf


class Vertice:
    def __init__(self, vertice) -> None:
        self.__profundidade = inf
        self.__vertice = vertice
        self.__adjacentesPesos = []
        self.__pai = inf
        self.__filho = inf

    def setAresta(self, u: int, peso: int) -> None:
        self.__adjacentesPesos.append([u, peso])

    def getAresta(self) -> list:
        return [i[0] for i in self.__adjacentesPesos]

    def getPeso(self) -> list:
        return [i[1] for i in self.__adjacentesPesos]

    def getArestaPeso(self) -> list:
        return self.__adjacentesPesos

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

    def setPai(self, pai: int) -> None:
        self.__pai = pai

    def getPai(self) -> int:
        return self.__pai

    def setFilho(self, filho: int) -> None:
        self.__filho = filho

    def getFilho(self) -> int:
        return self.__filho
