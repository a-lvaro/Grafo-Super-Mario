from grafo import Grafo
from bfs import Bfs
from dfs import Dfs
from prim import Prim
from topologica import Topologica


g = Grafo()
# g.bfs(53)
# g.mostrarProfundidade() -- não precisa usar

# print()

# g.dfs(53)
# g.mostraIdaVolta() -- não precisa usar

# print()


# g.topologia(53)
# g.mostrarTopologica() -- não precisa usar

g.prim(53)
