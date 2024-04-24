n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = 0
for i in range(n):
    d += abs(a[i] - b[i])

print('Yes') if d<=k and (k-d)%2==0 else print('No')