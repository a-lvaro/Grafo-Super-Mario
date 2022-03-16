from grafo import Grafo
from bfs import Bfs
from dfs import Dfs
from prim import Prim
from topologica import Topologica

'''
    DESENVOLVEDORES:

        Álvaro de Araújo    ra 120113
        Rômulo Barreto      ra 117477


    Trabalho I de Grafos em Super Mario World
    Professor Felippe Fernandes da Silva

'''

g = Grafo()


g.bfs(53)


input('\nPressione enter para continuar \n')


g.dfs(53)


input('\nPressione enter para continuar \n')


g.topologia(53)


input('\nPressione enter para continuar \n')


g.prim(53)
