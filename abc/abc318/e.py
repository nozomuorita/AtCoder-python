from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

dl, dr = defaultdict(int), defaultdict(int)
dl[a[0]] += 1
for i in range(1, n): dr[a[i]]+=1

s = 0
for key in list(dl.keys()):
    s += dl[key]*dr[key]

ans = 0
for i in range(1, n-1):
    ans += s - dl[a[i]]*dr[a[i]]
    
    s -= dl[a[i]]*dr[a[i]]
    dl[a[i]] += 1
    dr[a[i]] -= 1
    s += dl[a[i]]*dr[a[i]]

    #print(dl)
    #print(0, dr)
    #print(ans, s)
    #ans += s - dl[a[i]]*dr[a[i]]

    #s -= dl[a[i]]*dr[a[i]]
    #s -= dl[a[i+1]]*dr[a[i+1]]
    #dl[a[i]] += 1
    #dr[a[i+1]] -= 1
    #s += dl[a[i]]*dr[a[i]]
    #s += dl[a[i+1]]*dr[a[i+1]]

print(ans)
