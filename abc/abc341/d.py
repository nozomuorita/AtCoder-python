from math import lcm
n, m, k = map(int, input().split())
x = lcm(n, m)

left, right = 0, 10**30
while left<right:
    mid = (left+right)//2
    
    # mid以下に何個あるか
    score = (mid//n) + (mid//m)
    score -= 2*(mid//x)

    if score<k: left=mid+1
    else: right=mid

print(left)