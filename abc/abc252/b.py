n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

mx = max(a)
for i in b:
    if a[i-1]==mx: exit(print('Yes'))

print('No')