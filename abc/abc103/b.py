s = list(input())
t = list(input())

f = False
for i in range(len(s)):
    tmp = s.pop()
    s.insert(0, tmp)
    
    if s == t:
        f = True
        break
    
print('Yes' if f else 'No')