"""
8 14
a b 10
a c 9
a g 10
b f 20
b d 10
b c 2
f d 11
d e 9
d c 8
e n 100
c g 20
n c 11
n g 11
c a 10
a n
----------
130
"""
from collections import defaultdict
import heapq


def shortestPath(graph, src, dest):
    node = list()
    heapq.heappush(node, (0, src))
    while len(node) != 0:
        cost, ver = heapq.heappop(node)
        if ver == dest:
            return cost
        for neb, _ in graph[ver]:
            heapq.heappush(node, ((cost + _), neb))


v, e = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(e):
    u, v, w = map(str, input().split(' '))
    graph[u].append((v, int(w)))
src, dest = map(str, input().split(' '))
print(shortestPath(graph, src, dest))
