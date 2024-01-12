n, k = map(int, input().split())
a = list(map(int, input().split()))

def check(number):
    left, right = 0, n
    while left<right:
        mid = (left+right)//2
        if a[mid]==number: return mid+1
        if a[mid]<number: left=mid+1
        else: right=mid
    return left

ans = 0
for i in range(n):
    idx = check(a[i]+k)
    ans += (idx - (i+1))

print(ans)