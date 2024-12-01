t = int(input())
test = 1
count = 1
while t > 0:
    print(f'Test {count}:')
    siz = int(input())
    matrix = list()
    for i in range(siz):
        row = [int(x) for x in input().split(' ')]
        print(f'Row{i + 1}: {min(row)} {max(row)}')
        matrix.append(row)
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for c in range(siz):
        print(f'col{c + 1}: {min(matrix[c])} {max(matrix[c])}')
    count += 1
    t -= 1
