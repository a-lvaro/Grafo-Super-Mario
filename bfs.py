from cmath import inf


class Bfs:
    def __init__(self, grafo: object, verticeInicio: int) -> None:
        aux = []

        grafo.setProfundidade(verticeInicio, 0)
        aux.append(verticeInicio)

        while aux:
            u = aux.pop(0)

            for vertice in grafo.getAdjacentes(u):
                if grafo.getProfundidade(vertice) == inf:
                    aux.append(vertice)
                    grafo.setProfundidade(
                        vertice, grafo.getProfundidade(u) + 1)
