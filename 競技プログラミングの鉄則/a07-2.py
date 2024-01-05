d = int(input())
n = int(input())
l, r = [], []
diff = [0]*(d+2)
for i in range(n):
    l_, r_ = map(int, input().split())
    l.append(l_)
    r.append(r_)
    
    diff[l_] += 1
    diff[r_+1] -= 1

ans = [0]*(d+2)
ans[0] = 0
for i in range(1, d+1):
    ans[i] = ans[i-1] + diff[i]

for i in range(1, d+1): print(ans[i])