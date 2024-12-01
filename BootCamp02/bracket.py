st = list(input())
bracket = list()
flag = True
for i in st:
    if i in ['(', '{', '[']:
        bracket.append(i)
    if i in [')', ']', '}']:
        x = bracket.pop()
        if x == '(' and i == ')' or x == '[' and i == ']' or x == '{' and i == '}':
           pass
        else:
            flag = False
            break
if flag:
    print("YES")
else:
    print("NO")