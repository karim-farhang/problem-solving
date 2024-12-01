"""
2
7
120 1 0
600 200 30
999 120 80
2000 1 1
2230 800 10
2700 38 9999
2980 10 10
1
679 1572864 51200
----------------
321B / 110B
0B / 0B
849B / 9.79KB
---
1.5MB / 50KB
"""

t = int(input())
rt = []
units = ['B', 'KB', 'MB', 'GB', 'TB']
downtimeUP = 0
downTimeDow = 0
while t > 0:
    siz = int(input())
    download = 0
    upload = 0
    while siz > 0:
        time, down, up = [int(x) for x in input().split(' ')]
        download += down
        upload += up
        if (time / 1000) >= (down + up):
            download -= down
            upload -= up
            downtimeUP = up
            downTimeDow = down
            count = 0
            while download > 1024:
                download = download / 1024
                count += 1
            speed_down = str(round(download, 2)) + units[count]

            count = 0
            while upload > 1024:
                upload = upload / 1024
                count += 1
            speed_up = str(round(upload, 2)) + units[count]

            rt.append([speed_down+"/", speed_up])
            rt.append([str(0) + units[0]+"/", str(0) + units[0]])
            download = 0
            upload = 0
        siz -= 1
    count = 0
    while (download + downTimeDow) > 1024:
        download = download / 1024
        count += 1
    speed_down = str(round(download, 2)) + units[count]

    count = 0
    while (upload + downtimeUP) > 1024:
        upload = upload / 1024
        count += 1
    speed_up = str(round(upload, 2)) + units[count]

    rt.append([speed_down+'/', speed_up])
    rt.append(['---'])
    downtimeUP = 0
    downTimeDow = 0
    t -= 1

for i in range(len(rt) - 1):
    for j in range(len(rt[i])):
        print(rt[i][j], end='')
    print()
