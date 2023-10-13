n = int(input())
c = input()

r = c.count('R')
w = 0
wr = [[w, r]]

for i in range(n):
    if c[i]=='W':
        w += 1
        wr.append([w, r])
    else:
        r -= 1
        wr.append([w, r])
    
ans = 10**18    
for i in range(len(wr)):
    ans = min(ans, max(wr[i][0], wr[i][1]))

print(ans)