n, k = map(int, input().split())

def g1(x):
    x = sorted(str(x), reverse=True)
    x = int(''.join(x))
    return x

def g2(x):
    x = sorted(str(x))
    x = int(''.join(x))
    return x

def f(x):
    g_1 = g1(x)
    g_2 = g2(x)
    return g_1 - g_2

ans = n
for i in range(1, k+1):
    ans = f(ans)

print(ans)