"""
1
3
6
10-20-5,30-30-5
5
30-40-5,60-30-10
3
80-40-10,70-30-10
-----------------
0.404
2 1 1
"""
t = int(input().strip())
r = []
cars = []
while t > 0:
    stations = int(input().strip())
    ca = []
    ra = 0
    while stations > 0:
        distance = int(input().strip())
        inp = input().split(',')
        car = []
        ratio = []
        for c in range(len(inp)):
            car.append([int(x) for x in inp[c].split('-')])
            ratio.append((car[c][1] / car[c][2]) * car[c][0])
        get_car = max(ratio)
        car_num = ratio.index(get_car)
        ra += distance / car[ratio.index(get_car)][0]
        ca.append(car_num + 1)
        stations -= 1
    r.append([round(ra, 3)])
    r.append(ca)
    t -= 1

for i in range(len(r)):
    for j in range(len(r[i])):
        print(r[i][j], end=' ')
    print()
