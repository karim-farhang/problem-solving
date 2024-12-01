n = int(input())
num = list(map(int, input().split()))
for i in range(1,n):
    for j in range(1,n):
        print(j)
        if num[num[j]] == i:
            print(j)
            break
