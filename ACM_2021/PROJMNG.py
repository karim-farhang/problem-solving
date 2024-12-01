ts = int(input().strip())
resultTes = []
for i in range(ts):
    ta = input().strip()
    arr = ta.split(' ')
    add = sum([int(x) for x in arr if x.isdigit()])
    while ta != "":
        ta = input().strip()
        if len(ta) > 0:
            ta = ta.split(' ')
            for j in range(len(ta) - 1):
                if ta[j] in arr and ta[j + 1].isdigit():
                    add += int(ta[j + 1])
    resultTes.append(add)

for x in resultTes:
    print(x)
