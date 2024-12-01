rps = [x for x in input().strip()]
for i in range(len(rps)):
    if rps[i] == 'S':
        rps[i] = 'P'
    elif rps[i] == 'P':
        rps[i] = 'R'
    elif rps[i] == 'R':
        rps[i] = 'S'

psr = ''.join(rps)
print(psr)
