t = int(input().strip())
rt = []
while t > 0:
    one, tow, perTime = [int(x) for x in input().strip().split(' ')]
    for i in range(perTime):
        temp = one + tow
        one = tow
        tow = temp
    rt.append(tow)
    t -= 1

for t in rt:
    print(t)
