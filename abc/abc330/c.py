"""
・xの値を全探索
・片方の値について、2*(10**6)ほどまで見れば良い
・xを決めた時、d-(x**2)が最も良い(値が0となる)y**2である、これをscoreと置く
・なので、2乗した値がscoreに最も近くなる整数yを探す
・これは、scoreのルートをとったときの整数値であると言える(y**2が10に最も近くなるyは√10=3.112...で3または4のどちらかとなる)
・この二つの候補について、absを計算し、ansを更新
"""
d = int(input())
ans = float("inf")

for i in range(2*(10**6)+1):
    score = d - (i**2)
    if score<0: continue
    
    v1 = int(score**0.5)
    v2 = int(score**0.5)+1
    
    ans = min(ans, abs(score-(v1**2)))
    ans = min(ans, abs(score-(v2**2)))
    
print(ans)