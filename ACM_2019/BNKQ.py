"""
2 5
0 1
0 2
0 3
2 4
1 5
---------------
9
"""
from collections import defaultdict, deque

t = int(input())
rtc = list()
while t > 0:
    counter, customer = map(int, input().split())
    customers = defaultdict(deque)
    for i in range(customer):
        u, v = map(int, input().split())
        customers[u].append(v)
    coun = [0] * counter
    visited = defaultdict(bool)
    p = 0
    for i, j in customers.items():
        for _ in range(len(j)):
            if p == len(coun):
                p = 0
            coun[p] += j.popleft()
            p += 1
    time = sum(coun)
    arive = sum(customers.keys())
    # result = (time + arive) / len(coun)
    rtc.append(max(coun))
    t -= 1
for i in rtc:
    print(i)
