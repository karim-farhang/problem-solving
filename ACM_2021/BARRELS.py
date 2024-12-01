"""
2
25
1 2 5 20
32 40
20
0

10
100


"""
import math

t = int(input())
rt = []
while t > 0:
    x = int(input())
    inp = ' '
    su = 0
    while inp != '':
        inp = input()
        if inp != '':
            inp2 = inp.split(' ')
            su += sum([int(x) for x in inp2])
    rt.append(math.ceil(su / x))
    t -= 1

for j in rt:
    print(j)
