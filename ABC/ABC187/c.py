from collections import defaultdict
n = int(input())

s1 = defaultdict(int)
s2 = defaultdict(int)

for i in range(n):
    s = input()
    if s[0]=='!':
        s2[s[1:]] += 1
    else:
        s1[s] += 1
     
ans = 'satisfiable'   
for i in list(s1.keys()):
    if s2[i]>0:
        ans = i
        break
print(ans)