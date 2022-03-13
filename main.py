from grafo import Grafo
from bfs import Bfs
from dfs import Dfs
from prim import Prim
from topologica import Topologica
from prim2 import Prim2


g = Grafo()
# bfs = Bfs(g, 53)
# g.mostrarProfundidade()

# print()

# dfs = Dfs(g, 53)
# dfs.mostrar()

# print()

# topologica = Topologica(g, 53)
# topologica.mostrar()

Prim2(g, 1, 53)
