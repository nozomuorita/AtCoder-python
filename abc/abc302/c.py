from collections import defaultdict
import itertools

N, M = map(int, input().split())
S = []
for i in range(N):
    s = input()
    S.append(s)
    
# 事前にマッチ具合を計算
# 値は何文字変える必要があるか
dd = defaultdict(lambda: -1)
for i in range(N):
    for j in range(i+1, N):
        s1 = S[i]
        s2 = S[j]
        match = 0
        for n in range(M):
            if s1[n] == s2[n]:
                match += 1
        key = str(i) + str(j)
        dd[key] = M - match
        
pattern = list(itertools.permutations([_ for _ in range(N)]))
for p in pattern:
    for i in range(N-1):
        tmp1 = p[i]
        tmp2 = p[i+1]
        min_t = min(tmp1, tmp2)
        max_t = max(tmp1, tmp2)
        tmp = str(min_t) + str(max_t)
        #tmp = str(i) + str(i+1)
        if dd[tmp] != 1:
            break
        if (dd[tmp]==1) and (i==N-2):
            print('Yes')
            exit()
    
print('No')