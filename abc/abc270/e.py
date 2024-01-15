n, k = map(int, input().split())
a = list(map(int, input().split()))

# 何周すればk個に達するかを二分探索
left, right = 0, 10**13
while left<right:
    mid = (left+right)//2
    
    score = 0
    for i in range(n):
        score += min(mid, a[i])

    if score>=k: right=mid
    else: left=mid+1

left -= 1                   # left-1周はできるので、left-1周分だけ計算
for i in range(n):
    score = min(left, a[i])
    a[i] -= score
    k -= score
        
#  次の一周でkがゼロになるので一つずつ取っていく
for i in range(n):
    if k==0: break
    if a[i]>0:
        a[i]-=1
        k -= 1
        
print(*a)