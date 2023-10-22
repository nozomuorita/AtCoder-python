n, T = map(int, input().split())
t = list(map(int, input().split()))

ans = []
for i in range(len(t)):
    if len(ans)==0: ans.append([t[i], t[i]+T]); continue
    if t[i] > ans[-1][1]:
        ans.append([t[i], t[i]+T])
    else:
        ans[-1][1] = t[i]+T
        
ans2 = 0
for i, j in ans:
    ans2 += j-i
print(ans2)