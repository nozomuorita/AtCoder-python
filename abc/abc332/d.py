from itertools import permutations
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

ans = 10**18
pt1 = list(permutations(range(h)))
pt2 = list(permutations(range(w)))
for i in pt1:
    a2 = []
    for k in i: a2.append(a[k])
    for j in pt2:
        a3 = [[0]*w for _ in range(h)]
        for l in range(w):
            for p in range(h): a3[p][l]=a2[p][j[l]]
        if a3==b:
            score = 0
            for x in range(h):
                for y in range(x+1, h):
                    if i[x]>i[y]: score+=1
            for x in range(w):
                for y in range(x+1, w):
                    if j[x]>j[y]: score+=1

            ans = min(ans, score)

print(-1) if ans==10**18 else print(ans)
