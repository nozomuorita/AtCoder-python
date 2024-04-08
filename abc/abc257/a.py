N, X = map(int, input().split())

s = ''
n = 65
for i in range(26):
    for i in range(N):
        s += chr(n)
        
    n += 1
    
print(s[X-1])