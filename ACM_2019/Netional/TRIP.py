"""
1
4 6
0 1 1
1 2 1
2 3 1
3 0 1
0 2 5
1 3 5
3
1
2
3
---------
4
"""
t = int(input())
rtc = []
while t > 0:
    node, edge = [int(x) for x in input().split(' ')]
    edges = {}
    matrix = [[0] * (node + 1) for _ in range(node + 1)]
    for _ in range(edge):
        x, y, d = [int(x) for x in input().split(' ')]
        if x not in edges:
            edges[x] = [y]
            matrix[x][y] = d
        else:
            edges[x].append(x)
            matrix[x][y] = d
    employe = int(input())
    employee_home = []
    for _ in range(employe):
        employee_home.append(int(input()))
    employee_home = list(set(employee_home))
    employee_home.insert(0, 0)
    employee_home.append(0)


    def get_path(start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in edges:
            return []
        paths = []
        for nod in edges:
            if nod not in path:
                new_path = get_path(nod, end, path)
                for p in new_path:
                    paths.append(p)
        return paths


    cost = 0
    for i in range(len(employee_home) - 1):
        xp = get_path(employee_home[i], employee_home[i + 1])
        cos = []
        for i in range(len(xp)):
            for j in range(len(xp[i])):
                xxx = matrix[i][j]
                if xxx > 0:
                    cos.append(xxx)
        cost += min(cos)
    rtc.append(cost)
    t -= 1
for i in rtc:
    print(i)
