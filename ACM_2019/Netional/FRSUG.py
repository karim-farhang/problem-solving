"""
7
0 1 4
0 3 8
1 4 1
1 2 2
4 2 3
2 5 3
3 4 2
0
4
1
4
5
7

----------------------
4
5
9
----

"""
from collections import defaultdict
import heapq

edge = int(input())
graph = defaultdict(list)
for _ in range(edge):
    u, v, w = map(int, input().split(' '))
    graph[u].append((v, w))
start = int(input())
inp = '     '
frind = list()
while inp != '':
    inp = input()
    if inp != '':
        frind.append(int(inp))


def shortestPath(graph, src, dest):
    path = []
    heapq.heappush(path, (0, src))
    while len(path) != 0:
        currcost, currvtx = heapq.heappop(path)
        if currvtx == dest:
            return currcost
        for neigh, neighcost in graph[currvtx]:
            heapq.heappush(path, (currcost + neighcost, neigh))


frind = list(set(frind))
frind.insert(start, 0)
for i in range(1, len(frind)):
    x = shortestPath(graph, frind[0], frind[i])
    if x != None:
        print(x)
    else:
        print('-----')
