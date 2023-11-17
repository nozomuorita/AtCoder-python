"""
・90°ずつ左回転されていき、4つの向きで一致させることができるか判定
・そもそもsとtで#の数が違えば、不可なので注意
"""
n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]
tx, ty = -1, -1
s_sharp, t_sharp = 0, 0
for i in range(n):
    for j in range(n):
        if s[i][j]=="#": s_sharp+=1
        if t[i][j]=="#":
            t_sharp += 1
            if tx==-1 and ty==-1: tx, ty = i, j

if s_sharp!=t_sharp: exit(print('No'))

def rotate(p):
    #  90°左回転は、転置してから上下逆にする
    tp = []
    transposed = list(zip(*p))
    for i in transposed[::-1]:
        tp.append(list(i))
    return tp

for _ in range(4):
    sx, sy = -1, -1
    f = True
    for i in range(n):
        for j in range(n):
            if s[i][j]==".": continue
            
            if sx==-1 and sy==-1: sx, sy=i, j
            dx, dy = i-sx, j-sy
            
            if tx+dx<0 or tx+dx>=n or ty+dy<0 or ty+dy>=n: f=False
            if f and t[tx+dx][ty+dy]!="#": f=False
    
    if f: exit(print('Yes'))
    s = rotate(s)

print('No')