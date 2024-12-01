t = int(input())
while t > 0:
    count = 0
    num = int(input())
    numSt = str(num)
    for i in numSt:
        if int(i) != 0:
            if num % int(i) == 0:
                count += 1
    print(count)
    t -= 1
