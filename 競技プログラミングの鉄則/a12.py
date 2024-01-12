n, k = map(int, input().split())
a = list(map(int, input().split()))

# sec秒で印刷される枚数を計算
def check(sec):
    score = 0
    for i in range(n):
        score += sec//a[i]
    return score

left, right = 0, 10**9
while left<right:
    mid = (right+left)//2
    s = check(mid)
    if s>=k: right=mid
    else: left=mid+1
    
print(left)