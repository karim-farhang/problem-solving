for t in range(int(input())):
    L = int(input())
    ladders = []
    for i in range(L):
        a, b = map(int, input().strip().split())
        ladders.append([a, b])
    S = int(input())
    snakes = []
    for i in range(S):
        a, b = map(int, input().strip().split())
        snakes.append([a, b])

    ladders.extend(snakes)
    D = {}
    for a, b in ladders:
        D[a] = b
    V = set()  # visited squares
    S = set()
    S.add(1)
    moves = 0
    while 100 not in S:
        moves += 1
        S2 = set()
        for a in S:
            for d in range(1, 6 + 1):
                n = a + d
                if n in D:
                    n = D[n]
                if n in V:
                    continue
                V.add(n)
                S2.add(n)
        S = S2
    print(moves)
