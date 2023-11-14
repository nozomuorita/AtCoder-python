S = []
for i in range(10):
    s = input()
    S.append(s)
    
ab = []
for i in range(10):
    s = S[i]
    if '#' in s:
        ab.append(i+1)
        
A = min(ab)
B = max(ab)

s = S[A-1]
cd = []
for i in range(10):
    if s[i] == '#':
        cd.append(i+1)
        
C = min(cd)
D = max(cd)

print(A, B)
print(C, D)