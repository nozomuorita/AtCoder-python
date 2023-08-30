n = int(input())
x = list(map(int, input().split()))

x2 = x.copy()
x2.sort()

median = (x2[n//2] + x2[n//2-1]) / 2

for i in range(n):
    if x[i]<=median:
        print(x2[n//2])
    else:
        print(x2[n//2-1])