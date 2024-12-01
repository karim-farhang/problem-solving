"""
2
3 3
101
000
100
2 2
11
11
------------
Yes
No
"""


def check(matrix):
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in matrix:
        if matrix.count(i) > 1:
            matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
            return False
    return True


t = int(input())
res = list()
while t > 0:
    m, n = map(int, input().split(' '))
    matrix = list()
    for i in range(m):
        row = list(input())
        matrix.append(row)
    # transpose matrix
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    result = 'NO'
    for i in range(len(matrix)):
        removed = matrix[i]
        matrix.remove(removed)
        if check(matrix):
            result = 'YES'
            break
        matrix.insert(i, removed)
    res.append(result)
    t -= 1
for i in res:
    print(i)
