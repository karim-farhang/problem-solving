"""
3
you we
have are
sleep eat drink
"""
si = int(input())
inputStr = list()
for i in range(si):
    row = input().split(' ')
    inputStr.append(row)

inputStr.reverse()
inp = 0
for i in inputStr:
    res = ''
    for j in i:
        res += inputStr[inp] + [" "] + [j]
    print(*res)