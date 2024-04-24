h, w = map(int, input().split())
led = [[False]*w for _ in range(h)]

if h==1 or w==1: exit(print(max(h, w)))

d = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if i==0 and j==0: continue
        d.append([i, j])

ans = 0
for i in range(h):
    for j in range(w):
        for d1, d2 in d:
            if 0<=i+d1<h and 0<=j+d2<w:
                if led[i+d1][j+d2]: break
        else:
            ans += 1
            led[i][j] = True

print(ans)