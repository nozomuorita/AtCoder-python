from collections import defaultdict, deque

n, m = map(int, input().split())
roads = []
dic = defaultdict(list)

for i in range(m):
    l, d, k, c, a, b = map(int, input().split())
    a -= 1; b -= 1
    dic[b].append(i)
    roads.append([l, d, k, c, a, b])

ans = [-float("inf")] * n
ans[n-1] = float("inf")
q = deque([n-1])

while q:
    v = q.popleft()
    for idx in dic[v]:
        l, d, k, c, a, b = roads[idx]
        left, right = 0, k-1
        mx = -1
        while left<=right:
            mid = (left+right)//2
            t = l + (mid*d)
            if t+c <= ans[b]:
                left = mid+1
                mx = max(mx, mid)
            else:
                right = mid-1
        
        if mx==-1: continue
        t = l + (mx*d)
        if ans[a] < t:
            ans[a] = max(ans[a], t)
            q.append(a)

for i in range(n-1):
    if ans[i]==-float("inf"): print("Unreachable")
    else: print(ans[i])