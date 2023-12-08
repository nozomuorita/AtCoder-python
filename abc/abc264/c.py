import itertools
h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]

pattern1 = list(itertools.combinations(range(h1), h2)) # h1行の中からh2行だけ選択する行を選択
pattern2 = list(itertools.combinations(range(w1), w2))

for i in pattern1:
    a2 = [a[x] for x in i]
    for j in pattern2:
        a3 = [[] for _ in range(len(a2))]
        for k in j:
            for l in range(len(a2)):
                a3[l].append(a2[l][k])
        
        if a3==b: exit(print('Yes'))
        
print('No')