t = int(input())
rtc = list()
while t > 0:
    x, y = map(int, input().split(' '))
    list1 = list(map(int, input().split(' ')))
    list2 = list(map(int, input().split(' ')))
    rtc.append(list2)
    t -= 1
for i in rtc:
    print(*i)
