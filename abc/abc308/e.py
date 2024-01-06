n = int(input())
a = list(map(int, input().split()))
s = input()

m_cum = [[0]*3 for _ in range(n+1)]
x_cum = [[0]*3 for _ in range(n+1)]
for i in range(n):
    m_cum[i+1] = m_cum[i].copy()
    if s[i]=="M":
        m_cum[i+1][a[i]] += 1

for i in range(n-1, -1, -1):
    x_cum[i] = x_cum[i+1].copy()
    if s[i]=="X":
        x_cum[i][a[i]] += 1

def mex(lst):
    mex = 0
    lst.sort()
    for i in lst:
        if i==mex: mex+=1
    return mex
        
ans = 0
for i in range(n):
    if s[i]!="E": continue
    
    for j in range(3):
        for k in range(3):
            score = m_cum[i+1][j] * x_cum[i][k]
            ans += score * mex([j, k, a[i]])

print(ans)