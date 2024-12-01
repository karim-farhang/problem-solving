"""
1
3
I like it.
khili Khobish ast.
Mardom poor hastan.
"""
tc = int(input())
rtc = []
posataive = ['good', 'nice', 'like', 'mashallah', 'barakallah', 'tashakor', 'khobish', 'popular']
negative = ['bad', 'zesht', 'lier', 'manfi', 'impossible', 'mariz', 'poor', 'hunger']
while tc > 0:
    sent = int(input())
    pos = 0
    neg = 0
    for i in range(sent):
        x = input().split(' ')
        for j in x:
            if j.lower() in posataive:
                pos += 1
            if j.lower() in negative:
                neg += 1
    rtc.append([pos, neg])
    tc -= 1
print(f'Positive: {rtc[0][0]}, Negative: {rtc[0][1]}')
