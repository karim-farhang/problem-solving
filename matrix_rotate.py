def rotate(M):
    rows = len(M)
    cols = len(M[0])
    res = []
    for i in range(cols):
        temp = []
        for j in range(rows):
            temp.append(M[j][i])
        res.append(temp[::-1])
    return res


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 8, 9]
]
for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
x = rotate(matrix)
print('-----------------')
for i in x:
    for j in i:
        print(j, end=' ')
    print()

x = rotate(x)
print('-----------------')
for i in x:
    for j in i:
        print(j, end=' ')
    print()

"""
def matrixflip(m,d):
    if d=='h':
        m=myl
        for i in range(0,len(m),1):
                    m[i].reverse()
        return(m)
    elif d=='v':
        m=myl
        m.reverse()
        return(m)
    else:
       return(m)
"""