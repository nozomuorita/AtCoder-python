n, l = map(int, input().split())
amida = [input() for _ in range(l+1)]

for i in range(n):
    x, y = i*2, 0
    
    while y<=(l-1):
        if 0<=x-1<(2*n-1) and amida[y][x-1]=="-":
            x -= 2
            y += 1
        elif 0<=x+1<(2*n-1) and amida[y][x+1]=="-":
            x += 2
            y += 1
        else:
            y += 1
    
    if amida[-1][x]=="o":
        exit(print(i+1))