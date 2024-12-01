s1 = [int(i) for i in input().split(' ')]
s2 = [int(i) for i in input().split(' ')]
res = s1+s2
res.sort()
print(*res)