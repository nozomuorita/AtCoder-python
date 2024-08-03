from itertools import permutations
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x:x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

cd = [list(map(lambda x:x-1, map(int, input().split()))) for _ in range(m)]
p = permutations(range(n), n)
for i in p:
    dic = {}
    for j in range(n):
        dic[i[j]] = j
    
    g2 = [[] for _ in range(n)]
    for c, d in cd:
        g2[dic[c]].append(dic[d])
        g2[dic[d]].append(dic[c])

    for t in range(n):
        if sorted(g[t])!=sorted(g2[t]):
            break
    else:
        exit(print('Yes'))

print('No')