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
# g.mostraIdaVolta()

# print()

<<<<<<< HEAD
# topologica = Topologica()
# listaTopologica = topologica.topologica(g, 53)
# print('Lista de vertices pela Ordenação Topológica: \n', listaTopologica)

prim = Prim(g, 53)
=======
topologica = Topologica(g, 53)
topologica.mostrar()
>>>>>>> d9f035a784107ae809604bb35cd46990dccf3a38
