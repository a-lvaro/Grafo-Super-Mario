from cmath import inf
import queue


class Prim2:
    def __init__(self, grafo: object, peso: int, verticeInicio: int) -> None:

        aux = verticeInicio
        grafo.setPai(verticeInicio, -1)
        queue = grafo.getAdjacentes(verticeInicio)
        queue = max(queue)
        grafo.setFilho(aux, queue)

        while queue:
            grafo.setPai(queue, aux)
            aux = queue
            queue = grafo.getAdjacentes(queue)

            if grafo.getPai(aux) in queue:
                queue.remove(grafo.getPai(aux))

            if len(queue) != 0:
                queue = max(queue)
                grafo.setFilho(aux, queue)

        # printar
        aux = verticeInicio
        while aux:
            print(aux)
            if grafo.vertices[aux - 1].getFilho() != inf:
                aux = grafo.vertices[aux - 1].getFilho()
            else:
                aux = 0
