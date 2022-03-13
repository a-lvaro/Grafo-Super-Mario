from cmath import inf


class Prim:
    def __init__(self, vertices: list, posicao: int) -> None:
        aux = posicao
        vertices[posicao].setPai(-1)
        queue = vertices[posicao].getAresta()
        queue = max(queue)
        vertices[posicao].setFilho(queue)
        queue -= 1

        # print(vertices[posicao].getPai())
        # print(vertices[posicao].getFilho())

        while queue:
            vertices[queue].setPai(aux + 1)
            aux = queue
            queue = vertices[queue].getAresta()
            # queue = [i-1 for i in queue]

            if vertices[aux].getPai() in queue:
                queue.remove(vertices[aux].getPai())

            if len(queue) != 0:
                queue = max(queue)
                vertices[aux].setFilho(queue)
                queue -= 1

        # printar
        aux = posicao
        while aux:
            print(aux + 1)
            if vertices[aux].getFilho() != inf:
                aux = vertices[aux].getFilho()
                aux -= 1
            else:
                aux = 0
