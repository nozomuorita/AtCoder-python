N, T = map(int, input().split())
A = list(map(int, input().split()))

# 全曲の総時間
sum_a = sum(A)
t = 0

if T>sum_a:
    t0 = T % sum_a
else:
    t0 = T

for i in range(len(A)):
    if (t+A[i]) >= t0:
        ans1 = i + 1
        ans2 = t0 - t
        break
    else:
        t += A[i]
        
print(ans1, ans2)