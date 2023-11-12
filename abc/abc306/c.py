from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
ans = []

for i in range(len(A)):
    tmp = A[i]
    d[tmp] += 1
    if d[tmp] == 2:
        ans.append(tmp)
    
print(*ans)