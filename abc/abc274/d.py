n, x, y = map(int, input().split())
a = list(map(int, input().split()))

#  dpx[i][j]: i番目(x方向に移動するもの(奇数番目)に限る)まで決めて、x座標をjとすることができるか(j=10000を座標0とする)
dpx = [[False]*(2*(10**4)+100) for _ in range((n+1)//2)]
#  dpy[i][j]: i番目まで決めて、y座標をjとすることができるか(j=10000を座標0とする)
dpy = [[False]*(2*(10**4)+100) for _ in range(n//2+1)]

g = 10000
# x座標について
dpx[0][g+a[0]] = True
for i in range((n+1)//2-1):
    for j in range(2*(10**4)+100):
        if dpx[i][j]:
            # 2*(i+1)+1
            diff = a[2*(i+1)]
            dpx[i+1][j+diff] = True
            dpx[i+1][j-diff] = True
   
# y座標について     
dpy[0][g] = True
for i in range(n//2):
    for j in range(2*(10**4)+100):
        if dpy[i][j]:
            # (2*i)+1
            diff = a[(2*i)+1]
            dpy[i+1][j+diff] = True
            dpy[i+1][j-diff] = True
            
if dpx[-1][g+x] and dpy[-1][g+y]: print('Yes')
else: print('No') 