import math

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    count = 0
    for i in range(a, b + 1):
        j = math.sqrt(i)
        if j == int(j):
            count += 1
    print(count)
