k = int(input())
a, b = map(str, input().split())

A, B = 0, 0
n = 1
for i in reversed(range(len(a))):
    A += int(a[i]) * n
    n *= k

n = 1
for i in reversed(range(len(b))):
    B += int(b[i]) * n
    n *= k

print(A * B)