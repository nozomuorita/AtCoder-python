def ceil_div(x, y): return -(-x//y)
n, h = map(int, input().split())
a, b, c, d, e = map(int, input().split())

ans = float("inf")
# 普通の食事をi回
for i in range(n+1):
    j = ceil_div((n*e - h - ((b+e)*i)), d+e)
    if (n*e - h - ((b+e)*i))%(d+e)==0: j+=1
    if j<0: j=0
    score = (a*i) + (c*j)
    ans = min(ans, score)

print(ans)