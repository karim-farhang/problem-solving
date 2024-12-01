# -- Ford-Fulkerson algorith ---
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
    def searching_algo_BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False
    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        while self.searching_algo_BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow
n = int(input())
s, d, e = map(int, input().strip().split())
gr = [[0] * n for i in range(n)]
for i in range(e):
    u, v, w = map(int, input().strip().split())
    gr[u - 1][v - 1] = w
g = Graph(gr)
source = s-1
sink = d-1
print("Max Flow: %d " % g.ford_fulkerson(source, sink))
