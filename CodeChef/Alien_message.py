"""
1
7 7
742 357 357 910 854 854 945
707 812 588 700 798 224 735
889 910 840 840 812 602 945
693 224 679 224 763 777 735
910 945 896 693 896 896 910
763 728 805 798 735 784 770
840 840 602 910 903 840 364
---------------------------
"""
tc = int(input())
rtc = []
while tc > 0:
    r, c = [int(x) for x in input().split(' ')]
    message = []
    dycrep = []
    for i in range(r):
        x = [int(int(x) / 7) for x in input().split(' ')]
        message.append(x)

    for i in range(len(message)):
        for j in range(len(message[i])):
            if j % 2 == 0:
                message[j][i] -= 19
                print(chr(int(message[j][i])), end="")
            else:
                print(chr(int(message[j][i])), end="")
    tc -= 1
print(''.join(rtc))
