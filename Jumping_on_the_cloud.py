n, k = map(int, input().split())
c = list(map(int, input().split()))
i = 0
e = 100
while True:
    i += k
    l = i % n
    x = c[l]
    if x == 1:
        e -= 3
    else:
        e -= 1
    if l == 0:
        break
print(e)
