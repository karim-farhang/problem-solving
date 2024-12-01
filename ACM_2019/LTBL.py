"""
1
6
team1 [2 - 0] team3
team1 [1 - 1] team2
team2 [4 - 7] team3
team2 [0 - 0] team1
team3 [5 - 3] team1
team3 [6 - 1] team2
6
team1 [0 - 0] team3
team1 [3 - 1] team2
team2 [6 - 7] team3
team2 [0 - 0] team1
team3 [5 - 3] team1
team3 [6 - 1] team2
"""
tc = int(input())
rtc = []
while tc > 0:
    ru = int(input())
    sets = set()
    left = []
    right = []
    while ru > 0:
        t1, c1, c2, t2 = input().replace('-', '').replace('  ', ' ').replace('[', '').replace(']', '').split(' ')
        left.append([t1, int(c1)])
        right.append([t2, int(c2)])
        sets.add(t1)
        sets.add(t2)
        ru -= 1
    sets = list(sets)
    sets.sort()
    x = ''
    count = 0
    for c_tem in sets:
        x += c_tem + ','
        for i in range(6):
            count = 0
            for j in range(len(left)):
                # point
                if i == 0:
                    if c_tem == left[j][0] and left[j][1] > right[j][1]:
                        count += 3
                    if c_tem == left[j][0] and left[j][1] == right[j][1]:
                        count += 1
                    if c_tem == right[j][0] and left[j][1] < right[j][1]:
                        count += 3
                    if c_tem == right[j][0] and left[j][1] == right[j][1]:
                        count += 1
                # win
                if i == 1:
                    if c_tem == left[j][0] and left[j][1] > right[j][1]:
                        count += 1
                    if c_tem == right[j][0] and left[j][1] < right[j][1]:
                        count += 1
                # draw
                if i == 2:
                    if c_tem == left[j][0] and left[j][1] == right[j][1]:
                        count -= 1
                    if c_tem == right[j][0] and left[j][1] == right[j][1]:
                        count -= 1
                # loss
                if i == 3:
                    if c_tem == left[j][0] and left[j][1] < right[j][1]:
                        count += 1
                    if c_tem == right[j][0] and left[j][1] > right[j][1]:
                        count += 1
                # scored
                if i == 4:
                    if c_tem == left[j][0] and left[j][1] > 0:
                        count += left[j][1]
                    if c_tem == right[j][0] and right[j][1] > 0:
                        count += right[j][1]
                # received
                if i == 5:
                    if c_tem == left[j][0] and right[j][1] > 0:
                        count += right[j][1]
                    if c_tem == right[j][0] and left[j][1] > 0:
                        count += left[j][1]
            x += str(abs(count)) + ','
    rtc.extend(x.split(','))
    tc -= 1

result = []
rag = []
for i in range(len(rtc) - 1):
    rag.append(rtc[i])
    if len(rtc[i + 1]) > 4:
        result.append(rag)
        rag = []

result.append(rag)
for x in result:
    for y in x:
        print(y, end=' ')
    print()
