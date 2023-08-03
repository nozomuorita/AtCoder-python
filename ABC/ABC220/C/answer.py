n = int(input())
a = list(map(int, input().split()))
x = int(input())

sum_a = sum(a)

s = (x//sum_a) * sum_a
i = int((x//sum_a) * n)

for j in range(n):
    s += a[j]
    
    if s > x:
        break

print(i + j + 1)