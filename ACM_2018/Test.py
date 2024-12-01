def makegraph(propSnake, propLadder, numSnake, numLadder):
    graph = {}
    for num in range(1, 101):
        graph [num] = [[]]
        graph[num].append(float('inf'))
        for dice in range(1, 7):
            bAppend = False
            place =dice+num
            for Ladder in range(numLadder):
                if place == propLadder[Ladder][0]:
                    graph[num][0].append(propLadder[Ladder][1])
                    bAppend = True
            for Snake in range(numSnake):
                if place  == propSnake[Snake][0]:
                    graph[num][0].append(propSnake[Snake][1])
                    bAppend = True
            if bAppend is not True:
                graph[num][0].append(dice+num)
    return graph
def find_shortest_path(graph):
    graph[1][1] = 0
    for i in range(1, 100):
        for  j in graph[i][0]:
            try :
                if graph[i][1]+1 <= graph[j][1]:
                    graph[j][1] = graph[i][1] + 1
            except KeyError:
                continue
    return graph[100][1]
numT = int(input())
for i in range(numT):
    numLadder, numSnake = input().split(' ')
    numLadder = int(numLadder)
    numSnake = int(numSnake)
    propLadder = input().split()
    for j in range(len(propLadder)):
        l = propLadder[j].split(' ')
        l = [int(i) for i in l]
        propLadder[j] = l
    propSnake = input().split()
    for j in range(len(propSnake)):
        l = propSnake[j].split(' ')
        l = [int(i) for i in l]
        propSnake[j] = l
    g = makegraph(propSnake, propLadder, numSnake, numLadder)
    print(find_shortest_path(g))

