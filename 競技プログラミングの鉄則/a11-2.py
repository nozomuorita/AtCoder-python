n, x = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, n-1
while abs(right-left)>1:
    mid = (right+left)//2
    if a[mid]>x: right=mid
    else: left=mid

if a[right]==x: print(right+1)
elif a[left]==x: print(left+1)