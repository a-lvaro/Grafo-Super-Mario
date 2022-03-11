from imp import init_builtin
from mimetypes import init

from pip import main


class Prim:
    def __init__(self, grafo: object, verticeInicio: int) -> None:
        self.total = 0
        self.visitados = []
        self.visitados.append(verticeInicio)

        for vertice in self.visitados:
            for adjacente in grafo.getAdjacentes(vertice):
                if adjacente not in self.visitados:
                    self.visitados.append(adjacente)
                    self.total += 1
        print(self.total)
