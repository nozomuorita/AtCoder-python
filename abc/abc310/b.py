n, m = map(int, input().split())
goods = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==j: continue
        if goods[i][0]<goods[j][0]: continue
        
        ith, jth = set(goods[i][2:]), set(goods[j][2:])
        if len(ith & jth)!=len(ith): continue

        if goods[i][0]>goods[j][0]: exit(print("Yes"))
        else:
            for k in jth:
                if k not in ith: exit(print("Yes"))

print("No")
