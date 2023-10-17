from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

ans = 0
d = defaultdict(int)    # 各数字が何回登場したか
for i in range(n):
    ans += i - d[a[i]]
    d[a[i]] += 1
    
print(ans)