m = [[1, 2], [3, 4], [5, 6]]
for row in m:
    print(row)

rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
    print(row)

tr = [[rez[i][j] for i in range(len(rez))] for j in range(len(rez[0]))]

for col in tr:
    print(col)