from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
x = int(input())

d = defaultdict(lambda: False)
for i in b: d[i]=True

dp = [False]*(x+1)
dp[0] = True

for i in range(x+1):
    if dp[i]==False: continue
    
    for j in a:
        if i+j<=x and d[i+j]==False: dp[i+j]=True
        
print('Yes') if dp[-1] else print('No')