"""
1
2
A 4,B 2
5
S1,80,56
S5,100,0
S3,100,100
S4,56,89
S2,49,92
---------------------
S3,100,0,false
S1,72,0,false
S4,67,0,false
S5,66.66,2,false
S2,63.33,4,true
"""
t = int(input())
r = []
while t > 0:
    subjects = int(input())
    subject = [int(sub.split(' ')[1]) for sub in input().split(',')]
    number_of_student = int(input())
    result = []
    for current in range(number_of_student):
        flag = False
        inp = input().split(',')
        name = inp[0]
        inp.remove(name)

        inp = [float(inp[x]) for x in range(len(inp))]
        field = sum([subject[i] for i in range(len(inp)) if inp[i] < 50])
        average = sum([inp[i] * subject[i] for i in range(len(inp))]) / sum(subject)
        if field > sum(subject) / 2:
            flag = True
        average = str(average)
        if average.__contains__('.0'):
            average = average.replace('.0', '')
        else:
            average = round(float(average), 2)
        result.append([name, average, field, flag])
    r.append(result)
    t -= 1
r = sorted(r, key=lambda l: l[0][0][1], reverse=True)
for rt in r:
    for oi in rt:
        for aa in oi:
            print(aa, end=' ')
        print()
