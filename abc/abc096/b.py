a, b, c = map(int, input().split())
k = int(input())

s = a + b + c
mx = max([a, b, c])
s -= mx

s += mx * (2**k)
print(s)