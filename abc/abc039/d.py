"""
・各座標について、8方向を#とできるなら、そうする(s2のその点を#にして、s3のその点を含む8方向を#にする)
・s==s3なら可能であり、s2がその答えとなる
"""
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
s2 = [["."]*w for _ in range(h)]
s3 = [["."]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j]==".": continue
        
        ok = True
        for k in range(-1, 2):
            for l in range(-1, 2):
                if k==0 and l==0: continue
                if 0<=i+k<h and 0<=j+l<w:
                    if s[i+k][j+l]==".": ok=False
        
        if ok:
            s2[i][j] = "#"
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if 0<=i+k<h and 0<=j+l<w:
                        s3[i+k][j+l] = "#"

if s==s3:
    print("possible")
    for i in s2:
        print("".join(i))
else:
    print("impossible")