from cmath import inf
import queue


class Prim2:
    def __init__(self, grafo: object, peso: int, verticeInicio: int) -> None:

        aux = verticeInicio
        grafo.setPai(verticeInicio, -1)
        queue = grafo.getAdjacentes(verticeInicio)
        queue = max(queue)
        grafo.setFilho(aux, queue)

        # grafo.setPai(queue, aux)
        # aux = queue
        # queue = grafo.getAdjacentes(queue)
        # if grafo.getPai(aux) in queue:
        #     queue.remove(aux)
        # queue = max(queue)

        # grafo.setPai(queue, aux)
        # aux = queue
        # queue = grafo.getAdjacentes(queue)
        # if grafo.getPai(aux) in queue:
        #     queue.remove(aux)
        # queue = max(queue)

        # print(queue)

        # cont = 1
        # while queue:

        #     queue = grafo.getAdjacentes(queue)
        #     if aux in queue:
        #         queue.remove(aux)
        #     queue = max(queue)
        #     aux = queue

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

        # for vertice in grafo.vertices:
        #     print(vertice.getVertice(), ' : ',
        #           vertice.getPai(), ' : ', vertice.getFilho())
