from grafo import Grafo
from bfs import Bfs
from dfs import Dfs
from prim import Prim
from topologica import Topologica


g = Grafo()
# bfs = Bfs(g, 53)
# g.mostrarProfundidade()

# print()

# dfs = Dfs(g, 53)
# dfs.mostrar()

# print()

topologica = Topologica(g, 53)
topologica.mostrar()
