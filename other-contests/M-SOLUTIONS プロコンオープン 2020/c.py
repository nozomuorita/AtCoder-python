n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n-k):
    print('Yes') if a[i]<a[i+k] else print('No')