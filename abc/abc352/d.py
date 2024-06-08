from heapq import heapify, heappop, heappush
n, k = map(int, input().split())
p = list(map(int, input().split()))
idx = {}
for i in range(n):
    idx[p[i]] = i+1
if k==1:
    exit(print(0))
if n==k:
    exit(print(k-1))

q = []
q2 = []
mx, mn = -1, float("inf")
for i in range(1, k+1):
    heappush(q, idx[i])
    heappush(q2, -idx[i])
    if idx[i]>mx: mx=idx[i]
    if idx[i]<mn: mn=idx[i]
#print(idx)
left, right = 1, k
ans = mx - mn
discard = set()
for i in range(n-k):
    # mn_tmp = heappop(q)
    # mx_tmp = heappop(q2)
    # mx_tmp *= -1
    #print(i)
    if idx[left]==mn:
        # mn_tmp = heappop(q)        
        while len(q):
            mn_tmp = heappop(q)
            if mn_tmp!=mn and mn_tmp not in discard:
                break
        mn = mn_tmp
    if idx[left]==mx:
        # mx_tmp = heappop(q2)
        while 1:
            mx_tmp = heappop(q2)
            mx_tmp *= -1
            if mx_tmp!=mx and mx_tmp not in discard:
                break
        mx = mx_tmp
    discard.add(idx[left])
    left += 1
    right += 1
    
    if idx[right]<mn:
        mn = idx[right]
    if idx[right]>mx:
        mx = idx[right]
        
    heappush(q, idx[right])
    heappush(q2, -idx[right])
    ans = min(ans, mx-mn)
    #print(ans, mx, mn)
    
print(ans)
    
    
#     c.discard(idx[left])
#     c.add(idx[right+1])
    
#     mx, mn = max(c), min(c)
#     #print(mx, mn)
#     left += 1
#     right += 1
#     ans = min(ans, mx-mn)

# print(ans)