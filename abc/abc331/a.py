M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d==D: d=1; m+=1
else: d+=1

if m==(M+1): y+=1; m=1

print(y, m, d)