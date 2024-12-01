t = int(input())
while t > 0:
    s = input().split(' ')
    for i in s:
        if i == i[::-1]:
            print(i, end=' ')
    print()
    t -= 1
