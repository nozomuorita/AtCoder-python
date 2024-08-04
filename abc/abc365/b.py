n = int(input())
a = list(map(int, input().split()))
m = sorted(a, reverse=True)[1]
for i in range(n):
    if a[i]==m:
        exit(print(i+1))