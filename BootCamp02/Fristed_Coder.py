"""
7
1 7 2 2 2 4 4
"""
siz = int(input())
coder = list(map(int, input().split(' ')))
print(coder)
for i in range(siz):
    for j in range(siz):
         if coder[i] > coder[j] != 0:
            print(coder[j])
            coder[j] = 0
            break
print(sum(coder), *coder)
