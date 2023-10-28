"""
・n=10**7ならばO(nlogn)が通る(3sec)
"""
n = int(input())
lst = [0]*(n+1)

for i in range(1, n+1):
    j = i
    while j<=n:
        lst[j] += 1
        j += i

ans = 0
for i in range(1, n+1):
    ans += (i)*lst[i]

print(ans)