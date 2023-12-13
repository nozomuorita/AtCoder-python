from collections import defaultdict
n = int(input())
a = [int(input()) for i in range(n)]
a_set = sorted(list(set(a)))

d = defaultdict(int)
for i, x in enumerate(a_set):
    d[x] = i
    
ans = []
for i in a:
    ans.append(d[i])
    
for i in ans: print(i)