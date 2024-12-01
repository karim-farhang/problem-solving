t = int(input())
user = list()
for i in range(t):
    row = input().split(',')
    user.append(row)
count = 0
is_mutual = input().split(',')
all = list()
for i in user:
    if i[0] in is_mutual:
        all.append(i)
for i in all[0]:
    if i in all[1]:
        count += 1
print(count)
