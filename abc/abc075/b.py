h, w = map(int, input().split())
s = [input() for _ in range(h)]

d = [[i, j] for i in range(-1, 2) for j in range(-1, 2) if i!=0 or j!=0]

ans = []
for i in range(h):
    ms = ""
    for j in range(w):
        if s[i][j]=="#": ms+="#"; continue
        
        score = 0
        for d1, d2 in d:
            if 0<=(i+d1)<h and 0<=(j+d2)<w and s[i+d1][j+d2]=="#":
                score += 1
        ms += str(score)
    ans.append(ms)
    
for i in ans: print(i)