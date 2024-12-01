"""
3 4 3
untitled.png
345+
2344
3455
-----
trip2019.png
323
434
545
54+
-----
game.png
+10
210
351
445
-----
"""
# input
i, w, h = map(int, input().split(' '))
name = list()
image = list()
while i > 0:
    name.append(input())
    x = ''
    img = list()
    while x != '-----':
        x = input()
        if x != '-----':
            img.append(list(x))
    image.append(img)
    i -= 1

# rotate
for i in range(len(image)):
    while image[i][len(image[i]) - 1][0] != '+':
        temp = list()
        for x in range(len(image[i][0])):
            row = list()
            for y in range(len(image[i])):
                row.append(image[i][y][x])
            temp.append(row[::-1])
        image[i] = temp

# find doubcate
for matrix in image:
    if image.count(matrix) == 1:
        index = image.index(matrix)
        name.remove(name[index])
        image.remove(matrix)

# print result
for i in range(len(name) - 1, -1, -1):
    print(name[i])
