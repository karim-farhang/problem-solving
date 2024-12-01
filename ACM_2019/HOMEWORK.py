"""
1
2
20 30
40 60
"""
tc = int(input())
rtc = []
while tc > 0:
    siz = int(input())
    for i in range(siz):
        x, y = [int(x) for x in input().split(' ')]
        rtc.append([x + y, x * y])
    tc -= 1

for jj in rtc:
    for j in jj:
        print(j, end=' ')
    print()
