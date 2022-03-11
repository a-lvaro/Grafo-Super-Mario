from dfs import Dfs


class Topologica:
    def __init__(self) -> None:
        self.listaVoltas = []
        self.listaVertices = []

    def topologica(self, grafo: object, verticeInicial: int) -> list:
        Dfs(grafo, verticeInicial)

        for vertice in grafo.vertices:
            self.listaVoltas.append(grafo.getProfundidadeDFS(
                vertice.getVertice(), 'volta'))

        self.listaVoltas.sort(reverse=True)

        for volta in range(len(self.listaVoltas)):
            for vertice in grafo.vertices:
                if grafo.getProfundidadeDFS(vertice.getVertice(), 'volta') == self.listaVoltas[volta]:
                    self.listaVertices.append(vertice.getVertice())
                    print('Vertice: ', vertice.getVertice(),
                          ' - Valor de Volta: ', self.listaVoltas[volta])

        return self.listaVertices
