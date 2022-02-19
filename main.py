from grafo import Grafo
from bfs import Bfs
from dfs import Dfs

g = Grafo()
bfs = Bfs(g, 53)
g.mostrarProfundidade()

print('')

dfs = Dfs(g, 53)
g.mostraIdaVolta()
