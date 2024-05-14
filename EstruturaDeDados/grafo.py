class Grafo:
    def __init__(self):
        self.grafo = {}

    def add_aresta(self, u, v):
        if u not in self.grafo:
            self.grafo[u] = []
        self.grafo[u].append(v)
        #cria uma lista de arestas e dentro de cada indice dela, uma lista de vertices
        
    def dfs_recursive(self, v, visitado):
        visitado[v] = True
        print(v+1, end=' ')

        if v in self.grafo:
            for i in self.grafo[v]:
                if not visitado[i]:
                    self.dfs_recursive(i, visitado)
        #vai setando True em todas vertices que estão sendo visitadas
        #vai visitando todas vertices recursivamente

    def dfs(self, start):
        visitado = {v: False for v in self.grafo}
        self.dfs_recursive(start, visitado)
        #seta Falso em todas vertices e começa a chamada recursiva de vertices 

g = Grafo()

g.add_aresta(0,1)
g.add_aresta(1,2)
g.add_aresta(1,3)
g.add_aresta(2,0)
g.add_aresta(3,0)
g.add_aresta(3,1)
g.add_aresta(4,5)
g.add_aresta(4,6)
g.add_aresta(5,1)
g.add_aresta(6,3)

print("Busca profundidade:")
g.dfs(0)
