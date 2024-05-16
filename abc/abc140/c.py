n = int(input())
b = list(map(int, input().split()))

a = [10**8]*n
for i in range(n-1):
    a[i] = min(a[i], b[i])
    a[i+1] = min(a[i+1], b[i])

print(sum(a))