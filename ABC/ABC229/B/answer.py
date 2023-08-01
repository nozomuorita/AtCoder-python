a, b = map(str, input().split())

length = min(len(a), len(b))

# 同じくらいを足して、10を超えるなら繰り上がる
for i in range(1, length+1):
    if int(a[-i]) + int(b[-i]) >= 10:
        print('Hard')
        exit()

print('Easy')