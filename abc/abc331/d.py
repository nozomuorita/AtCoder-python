# Unsolve
n, q = map(int, input().split())
p = [input() for _ in range(n)]
black = 0
for i in p: black+=i.count("B")
row, col = [], []
for i in range(n): row.append(p[i].count("B"))
for i in range(n):
    tt = 0
    for j in range(n):
        if p[j][i]=="B": tt+-1
    col.append(tt)

for _ in range(q):
    a, b, c, d = map(int, input().split())
    
    s1 = (c-a+1)//n
    r1 = (c-a+1)%n
    s2 = (d-b+1)//n
    r2 = (d-b+1)%n
    print(s1, r1, s2, r2)
    if s1>=1 and s2>=1:
        ans = black*(s1*s2)
    #print(ans)
    if r1>=1:
        if a%n!=0:
            for i in range(a%n, n):
                ans += row[i]*s2
        if c%n!=(n-1):
            for i in range(c%n+1):
                ans += row[i]*s2
    #print(ans)
    if r2>=1:  
        if b%n!=0:
            for i in range(b%n, n):
                ans += col[i]*s1
        if d%n!=(n-1):
            for i in range(d%n+1):
                ans += col[i]*s1
    #print(ans)
    
    # for i in range(a%n, n):
    #     for j in range(b%n, n):
    #         if p[i][j]=="B": ans+=1
    # for i in range(a%n, n):
    #     for j in range(d%n+1):
    #         if p[i][j]=="B": ans+=1
    # for i in range(c%n+1):
    #     for j in range(b%n, n):
    #         if p[i][j]=="B": ans+=1
    # for i in range(c%n+1):
    #     for j in range(d%n+1):
    #         if p[i][j]=="B": ans+=1
    print(ans)
