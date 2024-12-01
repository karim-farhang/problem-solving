"""
3
spaghetti salad
chicken cheese
ananas banana
-------------
spaghettilad
chickenese
bananas
"""
tc = int(input())
rtc = []
while tc > 0:
    food1, food2 = [list(x) for x in input().split(' ')]
    newF = []
    if len(food1) > len(food2):
        for i in food1:
            if i in food2:
                food2.remove(i)
        newF = food1 + food2
    if len(food2) > len(food1):
        for i in food2:
            if i in food1:
                food1.remove(i)
        newF = food2 + food1
    if len(food2) == len(food1):
        for i in food1:
            if i in food2:
                food2.remove(i)
        newF = food2 + food1
    rtc.append(''.join(newF))
    tc -= 1

for i in rtc:
    print(i)
