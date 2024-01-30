from collections import deque
n = int(input())
a, b = [-1]*(2*n+1), [-1]*(2*n+1)
for i in range(n):
    _ = sorted(list(map(int, input().split())))
    a[_[0]], b[_[1]] = i, i

q = deque()
for j in range(1, 2*n+1):
    if a[j]!=-1:
        q.append(a[j])
    elif b[j]!=-1:
        p = q.pop()
        if p!=b[j]:
            exit(print('Yes'))

print('No')