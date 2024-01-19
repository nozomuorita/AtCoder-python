"""
・aiはなるべく大きく、ajはaiの半分に近いほど良い
・aiは最大とする(固定)
・aiに最も近いajをfor文で探す
"""
n = int(input())
a = sorted(list(map(int, input().split())))

ai, aj = a[-1], a[0]
diff = abs(ai/2 - aj)
for i in range(1, n):
    if diff > abs(ai/2 - a[i]):
        diff = abs(ai/2 - a[i])
        aj = a[i]

print(ai, aj)