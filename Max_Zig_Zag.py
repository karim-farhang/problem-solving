arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
size = len(arr)
s = 0
for i in range(len(arr)):
    m = 0
    for j in range(len(arr[i])):
        if j % 2 == 0:
            m += arr[j][i]
            print('\t', arr[j][i])
        elif i > 0:
            m += arr[j][i - 1]
            print(arr[j][i-1])
    s = max(s, m)
    print()
print(s)
