x, y, z = map(int, input().split())
if x<0:
    x *= -1
    y *= -1
    z *= -1

if y>x: print(abs(x))
elif 0<y<x:
    if 0<z<y: print(abs(x))
    elif y<z: print(-1)
    elif z<0: print((2*abs(z))+abs(x))
elif y<0: print(abs(x))
