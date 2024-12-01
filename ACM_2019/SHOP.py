"""
3
235
5:10,10:6,20:4,50:3
370
10:4,5:20,40:4,70:3,100:2,50:5
172
10:4,5:20,40:4,70:3,100:2,50:5
-------------------------------
Customer1:
50 3
20 4
5 1
Customer2:
100 2
70 2
10 3
Customer3:
Impossible
"""
tc = int(input())
rtc = []
while tc > 0:
    back = int(input())
    money = [[int(y) for y in x.split(':')] for x in input().split(',')]
    money.sort(key=lambda x: x[0], reverse=True)
    print(money)
    result = []
    count = 0
    for i in range(len(money)):
        while back >= money[i][0] and money[i][1] > 0:
            back -= money[i][0]
            money[i][1] -= 1
            count += 1
        if count > 0:
            result.append([money[i][0], count])
            count = 0
    if 0 < back < money[-1][0]:
        result.clear()
        result.append(['imposable'])
    rtc.append(result)
    tc -= 1

for i in range(len(rtc)):
    print(f'Customer{i + 1}:')
    for j in range(len(rtc[i])):
        for p in range(len(rtc[i][j])):
            print(rtc[i][j][p], end=' ')
        print()
