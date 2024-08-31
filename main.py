class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def Kruskal(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((weight, int(u), int(v)))
    edges.sort()
    
    n = len(graph)
    uf = UnionFind(n)
    
    mst = []
    mst_weight = 0
    
    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, "Peso: " + str(weight)))
            mst_weight += weight
    
    print("Kruskal:")
    print("Arestas:", mst)
    print("Peso total:", mst_weight)

def Prim(graph):
    import heapq

    start_node = "0"
    visited = set(start_node)
    min_heap = [(weight, start_node, to) for to, weight in graph[start_node].items()]
    heapq.heapify(min_heap)

    mst = []
    mst_weight = 0

    while min_heap:
        weight, frm, to = heapq.heappop(min_heap)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, " Peso: " + str(weight)))
            mst_weight += weight
            
            for to_next, weight in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(min_heap, (weight, to, to_next))

    print("Prim:")
    print("Arestas:", mst)
    print("Peso total:", mst_weight)

def main(): 
    graph = { 
        "0": {"1" : 6, "5" : 8 },
        "1": {"0" : 6, "5": 3, "6" : 7 },
        "2" : {"1" : 6, "3" : 8, "6" : 3, "7" : 3},
        "3" : {"2": 7 , "4": 5,"7" : 2, "8" : 4},
        "4" : {"3": 5,"8": 5,"9": 2},
        "5" : {"0": 8,"1": 3,"6": 9},
        "6" : {"1": 7,"2": 3,"5": 9,"7": 4},
        "7" : {"2": 3, "3": 2, "6": 4, "8": 6},
        "8" : {"3": 4,"4": 5,"7": 6,"9": 3},
        "9" : {"4": 2,"8": 3}
        }
    
    Prim(graph)
    Kruskal(graph)
    
        
if __name__ == '__main__':
    main()