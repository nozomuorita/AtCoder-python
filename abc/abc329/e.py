from collections import deque
n, m = map(int, input().split())
s = list(input())
t = list(input())

if m==1:
    if len(set(s))==1 and s[0]==t[0]: exit(print('Yes'))
    else: exit(print('No'))

q = deque()
for i in range(n-m+1):
    if s[i]==s[0]:
        for j in range(1, m):
            if s[i+j]!=t[j]: break
        else:                        #  breakしなかったらelse文に入る
            q.append(i)

used = set()                         #  すでに見たidxを入れる

while q:
    idx = q.popleft()
    used.add(idx)
    for i in range(m):
        s[idx+i] = "#"
        
    for i in range(idx+1, min(idx+m, n-m+1)):
        if i in used: continue
        for j in range(m):
            if (s[i+j]!="#" and s[i+j]!=t[j]): break
        else:
            q.append(i)
    
    for i in range(max(idx-m+1, 0), idx):
        if i in used: continue
        for j in range(m):
            if (s[i+j]!="#" and s[i+j]!=t[j]): break
        else:
            q.append(i)
                    
ans = ["#"]*n
print('Yes') if s==ans else print('No')