def findCount(chess):
    row, colm = 0, 0
    counter = 0
    for i in range(len(chess)):
        for j in range(len(chess[i])):
            if chess[i][j] == 'Q':
                row = i
                colm = j
                break

    # right
    for i in range(colm, len(chess[row])):
        if chess[row][i] == '0':
            counter += 1
            chess[row][i] = 'r'
        if chess[row][i] == 'X':
            break

    # left
    for i in range(colm-1, -1, -1):
        if chess[row][i] == '0':
            counter += 1
            chess[row][i] = 'l'
        else:
            break

    # bottom
    for i in range(colm, len(chess)):
        if chess[i][colm] == '0':
            counter += 1
            chess[i][colm] = 'b'
        if chess[i][colm] == 'X':
            break

    # top
    for i in range(colm, -1, -1):
        if chess[i][colm] == '0':
            counter += 1
            chess[i][colm] = 't'
        if chess[i][colm] == 'X':
            break

    # bottom left
    j = colm
    for i in range(row, -1, -1):
        if chess[j][i] == '0':
            counter += 1
            chess[j][i] = 'bl'
        if chess[j][i] == 'X':
            break
        j += 1

    # bottom right
    j = row
    for i in range(row, len(chess)):
        if chess[i][j] == '0':
            counter += 1
            chess[i][j] = 'br'
        if chess[i][j] == 'X':
            break
        j += 1

    # top right
    j = row
    for i in range(row, -1, -1):
        if chess[i][j] == '0':
            counter += 1
            chess[i][j] = 'tr'
        if chess[i][j] == 'X':
            break
        j += 1

    # top left
    j = row
    for i in range(row, -1, -1):
        if chess[i][j] == '0':
            counter += 1
            chess[i][j] = 'tl'
        if chess[i][j] == 'X':
            break
        j += 1
    for i in chess:
        print(i)
    return counter


tc = int(input())
rtc = []
while tc > 0:
    count = 0
    chess = []
    for i in range(8):
        line = input()
        line = list(line)
        chess.append(line)
    rtc.append(findCount(chess))
    tc -= 1
for i in rtc:
    print(i)
