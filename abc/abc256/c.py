"""
・9マスのうち左上の4マスを決定することで条件を満たす9マスとなりうるかが判定できる
・よって、左上の4マスを全探索する
"""
h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
for a in range(1, 29):
    for b in range(1, 29):
        for d in range(1, 29):
            for e in range(1, 29):
                c = h1-a-b
                f = h2-d-e
                
                if (c<1) or (f<1): continue
                
                g = w1-a-d
                h = w2-b-e
                i = w3-c-f
                if (g<1) or (h<1) or (i<1): continue
                if (g+h+i)==h3:
                    ans += 1
                
print(ans)