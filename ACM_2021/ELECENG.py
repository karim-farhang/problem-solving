"""
2
2 4
0,13,12,4
13,0,3,8
12,3,0,7
4,8,7,0
2 5
0,2,6,9,8
2,0,4,10,11
6,4,0,5,12
9,10,5,0,7
8,11,12,7,0
-----------------
4
1,2
7
1,4
"""
T, V = [int(x) for x in input().split(' ')]
adj_matrix = []
edges = {}
for _ in range(V):
    row = [int(x) for x in input().split(',')]
    adj_matrix.append(row)
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix)):
        u = adj_matrix[i][j]
        if u > 0:
            if i not in edges:
                edges[i] = [j]
            else:
                edges[i].append(j)
for q, w in edges.items():
    print(q, w)
