n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

d = 10**18

for i in range(n):
    tmp = t-h[i]*0.006
    if abs(a-tmp)<d:
        d = abs(a-tmp)
        ans = i+1
        
print(ans)