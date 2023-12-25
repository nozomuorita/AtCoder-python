from collections import deque
n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
num = k//2
q = deque()
for i in range(num):
    q.append(abs(a[2*i+1]-a[2*i]))
    ans += abs(a[2*i+1]-a[2*i])

if k%2==0: exit(print(ans))

tmp = ans
for i in range(num):
    score = q.pop()
    tmp -= score
    s = abs(a[(k-1)-(2*i)]-a[(k-1)-(2*i+1)])
    tmp += s
    ans = min(ans, tmp)

print(ans)