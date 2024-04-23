deg, dis = map(int, input().split())

if 112.5<=deg<337.5:
    dir = "NNE"
elif 337.5<=deg<562.5:
    dir = "NE"
elif 562.5<=deg<787.5:
    dir = "ENE"
elif 787.5<=deg<1012.5:
    dir = "E"
elif 1012.5<=deg<1237.5:
    dir = "ESE"
elif 1237.5<=deg<1462.5:
    dir = "SE"
elif 1462.5<=deg<1687.5:
    dir = "SSE"
elif 1687.5<=deg<1912.5:
    dir = "S"
elif 1912.5<=deg<2137.5:
    dir = "SSW"
elif 2137.5<=deg<2362.5:
    dir = "SW"
elif 2362.5<=deg<2587.5:
    dir = "WSW"
elif 2587.5<=deg<2812.5:
    dir = "W"
elif 2812.5<=deg<3037.5:
    dir = "WNW"
elif 3037.5<=deg<3262.5:
    dir = "NW"
elif 3262.5<=deg<3487.5:
    dir = "NNW"
else:
    dir = "N"

dis = int(dis/6+0.5)
if dis<=2:
    w = 0
elif 3<=dis<=15:
    w = 1
elif dis<=33:
    w = 2
elif dis<=54:
    w = 3
elif dis<=79:
    w = 4
elif dis<=107:
    w = 5
elif dis<=138:
    w = 6
elif dis<=171:
    w = 7
elif dis<=207:
    w = 8
elif dis<=244:
    w = 9
elif dis<=284:
    w = 10
elif dis<=326:
    w = 11
else:
    w = 12

if w==0: dir="C"
print(dir, w)