n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

# すべて燃え尽きる時間t
s = 0
for i in range(n):
    s += ab[i][0] / ab[i][1]

t = s / 2

# 時刻tでいる地点を左端から求めていく
t2 = 0
j = 0
while j<n:
    if t2+(ab[j][0]/ab[j][1]) > t:
        break
    t2 += ab[j][0] / ab[j][1]
    j += 1

ans = 0
t2 = 0
for i in range(j):
    ans += ab[i][0]
    t2 += ab[i][0] / ab[i][1]
    
e_t = t - t2
ans += e_t * ab[j][1]

print(ans)