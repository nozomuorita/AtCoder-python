"""
・各区間において、aの数=tの数 and cの数=gの数であればOK
・各区間において、各文字が何個出現するのかは累積和で計算
"""
n, s = map(str, input().split())
n = int(n)
cum = []
cum.append([0, 0, 0, 0])
for i in range(n):
    p = cum[i].copy()
    if s[i]=='A': cum.append(p); cum[i+1][0] += 1
    elif s[i]=='T': cum.append(p); cum[i+1][1] += 1
    elif s[i]=='C': cum.append(p); cum[i+1][2] += 1
    elif s[i]=='G': cum.append(p); cum[i+1][3] += 1

ans = 0

for i in range(1, n+1):
    for j in range(i+1, n+1):
        a = cum[j][0] - cum[i-1][0]
        t = cum[j][1] - cum[i-1][1]
        c = cum[j][2] - cum[i-1][2]
        g = cum[j][3] - cum[i-1][3]
        
        if a==t and c==g: ans += 1
                
print(ans)