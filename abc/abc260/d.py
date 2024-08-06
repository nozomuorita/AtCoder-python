from sortedcontainers import SortedSet
n, k = map(int, input().split())
p = list(map(int, input().split()))

ss = SortedSet()
dic = {}
dic2 = {}
card = [(-1, -1)] * (n+1)
cnt = 0

for i in range(n):
    idx = ss.bisect(p[i])
    if idx==len(ss):
        card[p[i]] = (cnt, 1)
        dic2[cnt] = set([p[i]])
        cnt += 1
    else:
        card[p[i]] = (card[ss[idx]][0], card[ss[idx]][1]+1)
        dic2[card[ss[idx]][0]].add(p[i])
        ss.discard(ss[idx])
    
    ss.add(p[i])
    
    if card[p[i]][1]==k:
        dic[card[p[i]][0]] = i+1
        for j in dic2[card[p[i]][0]]:
            ss.discard(j)
    
    # print(ss)
    # print(card)
    # print(dic)
    # print(dic2)
    # print("###########")

ans = [-1] * (n+1)
for i in range(n):
    try:
        ans[p[i]] = dic[card[p[i]][0]]
    except:
        pass

for i in ans[1:]: print(i)