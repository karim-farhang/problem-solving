tc = int(input())
rtc = []
while tc > 0:
    rtc.append([int(x) for x in input().replace(' ', '').split(',') if int(x) % 4 == 0])
    tc -= 1

for y in rtc:
    for x in y:
        print(x, end=' ')
