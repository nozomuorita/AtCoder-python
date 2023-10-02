a, b, n = map(int, input().split())

def f(x):
    s = ((a*x)//b) - (a * (x//b))
    return s

if b-1 <= n:
    ans = f(b-1)
else:
    ans = f(n)
print(ans)