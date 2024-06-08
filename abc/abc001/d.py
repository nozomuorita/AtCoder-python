from collections import defaultdict
n = int(input())
ans = []
t = defaultdict(int)
for i in range(n):
    s = input()
    s, e = s.split("-")
    s = int(s) - (int(s)%5)
    e = int(e) + ((5 - int(e)%5)%5)
    if str(e)[-2:]=="60":
        e = e - 60 + 100

    t[s] += 1
    t[e] -= 1

cnt = 0
for key in sorted(list(t.keys())):
    if cnt==0:
        cur = str(key).zfill(4) + "-"
    
    cnt += t[key]
    
    if cnt==0:
        cur += str(key).zfill(4)
        ans.append(cur)

for i in ans: print(i)