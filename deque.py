x = []
for i in range(10):
    x.append(i)
    print(i, end=' ')

print()
while x:
    print(x.pop(), end=' ')
