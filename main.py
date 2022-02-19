from grafo import Grafo
from bfs import Bfs
from dfs import Dfs
from topologica import Topologica

g = Grafo()
bfs = Bfs(g, 53)
g.mostrarProfundidade()

print('\n')

dfs = Dfs(g, 53)
g.mostraIdaVolta()

print('\n')

topologica = Topologica()
listaTopologica = topologica.topologica(g, 53)
print('Lista de vertices pela Ordenação Topológica: \n', listaTopologica)
