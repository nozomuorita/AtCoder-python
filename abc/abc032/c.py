"""しゃくとり法"""
n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]

if 0 in s: exit(print(n))

ans = 0
left, right = 0, 0
v = s[0]
while left!=n-1:
    while right+1<n and v*(s[right+1])<=k:
        right += 1
        v *= s[right]
    
    #print(left, right)
    if v<=k: ans = max(ans, right-left+1)
    
    if left==right and left<(n-1):
        v //= s[left]
        left += 1
        right += 1
        v *= s[left]
        while s[left]>k and left!=(n-1):
            v //= s[left]
            left += 1
            right += 1
            v *= s[left]
    else:
        if left!=right:
            v //= s[left]
            left+=1

if s[left]<=k: ans=max(ans, 1)

print(ans)