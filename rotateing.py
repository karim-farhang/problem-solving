"""
4
+23
123
123
123
"""


def rotate(a):
    r = len(a)
    c = len(a[0])
    result = []
    for i in range(c):
        row = []
        for j in range(r):
            row.append(a[j][i])
        result.append(row[::-1])
    return result


def filp_horzontal_and_Virtical(a):
    return [[a[j][i] for i in range(len(a[0]))][::-1] for j in range(len(a))][::-1]


def filp_horzontal(a):
    return [[a[j][i] for i in range(len(a[0]))][::-1] for j in range(len(a))]


a = []
siz = int(input())
for i in range(siz):
    a.append(list(input()))

for i in a:
    print(i)

count = 0
while count != 360:
    count += 90
    print(f' {count} debugger-----')
    a = filp_horzontal(a)
    for i in a:
        print(i)
