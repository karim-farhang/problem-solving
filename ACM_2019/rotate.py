mat = [
    ['3', '4', '5', '+'],
    ['2', '3', '4', '4'],
    ['3', '4', '5', '5']
]


def rotate(mat):
    temp = list()
    for i in range(len(mat[0])):
        x = list()
        for j in range(len(mat)):
            x.append(mat[j][i])
        temp.append(x[::-1])
    return temp


def transpose(img):
    return [[img[i][j] for i in range(len(img))] for j in range(len(img[0]))]


while mat[len(mat) - 1][0] != '+':
    mat = rotate(mat)

for i in mat:
    print(*i)

print(len(mat[0]))
if len(mat[0]) != 4:
    mat = transpose(mat)

print('\n\n')
for i in mat:
    print(*i)

mat = transpose(mat)
print('\n\n')
for i in mat:
    print(*i)
