"""
2
a=Khaled
b=${a} is ${c} year’s old
c=25
---
Hi, ${b}
---
---
---
----------------
Hi, Khaled is 25 year’s old
[an empty line for second test case]
"""


def make_string(string, start):
    result = ''
    if start=='---':
        return "empty"
    for k, v in string.items():
        v = list(v)
        for i in range(len(v) - 2):
            if v[i] == '$':
                key = v[i + 2]
                v[i + 2] = dec[key]
                dec[k] = ''.join(v)
    start = list(start)
    for j in range(len(start) - 2):
        if start[j] == '$':
            key = start[j + 2]
            start[j + 2] = dec[key]
    result = ''.join(start)
    result = result.replace('$', '')
    result = result.replace('{', '')
    result = result.replace('}', '')
    return result


dec = {
    'a': 'Khalid',
    'b': '${a} is ${c} year’s old',
    'c': '25'
}

start = 'Hi, ${b}'
print(make_string(dec, start))

t = int(input())
rt = []
inp = ''
decs = {}
while t > 0:
    while inp != '---':
        inp = input()
        if inp.__contains__('='):
            x, y = inp.split('=')
            decs[x] = y
    start = input()
    rt.append(make_string(decs, start))
    t -= 1
print()
for i in rt:
    print(i)