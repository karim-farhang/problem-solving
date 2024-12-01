t = int(input())
count = 1
while t > 0:
    name = input().split(',')
    socr = [int(i) for i in input().split(',')]
    s_max = max(socr)
    s_min = min(socr)
    print(f'Test {count}:')
    print(f'{name[socr.index(s_max)]} {s_max}')
    print(f'{name[socr.index(s_min)]} {s_min}')
    count += 1
    t -= 1
