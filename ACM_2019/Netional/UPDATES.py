installed = list(map(str, input().split(',')))
server = list(map(str, input().split(',')))
update_nedded = list()
for i in installed:
    for j in server:
        if i in j or i == j or j > i:
            if j not in update_nedded:
                update_nedded.append(j)
print(*update_nedded)
