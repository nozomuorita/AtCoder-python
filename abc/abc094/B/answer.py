n, m, x = map(int, input().split())
a = list(map(int, input().split()))

num1, num2 = 0, 0
for i in range(m):
    if a[i]<x:
        num1 += 1
    else:
        num2 += 1
print(min(num1, num2))