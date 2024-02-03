"""やるだけ"""
w, h, d = map(str, input().split())
w = int(w)-1; h = int(h)-1
c = [input() for _ in range(9)]

ans = ""
for i in range(4):
    ans += c[h][w]
    
    if d=="R":
        if 0<=w+1<9: w+=1
        else:
            w-=1
            d = "L"
    elif d=="L":
        if 0<=w-1<9: w-=1
        else:
            w+=1
            d = "R"
    elif d=="U":
        if 0<=h-1<9: h-=1
        else:
            h+=1
            d = "D"
    elif d=="D":
        if 0<=h+1<9: h+=1
        else:
            h-=1
            d = "U"
    elif d=="RU":
        if 0<=h-1<9 and 0<=w+1<9:
            w += 1
            h -= 1
        else:
            if h-1<0 and w+1>=9:
                h += 1
                w -= 1
                d = "LD"
            elif h-1<0:
                h += 1
                w += 1
                d = "RD"
            elif w+1>=9:
                h -= 1
                w -= 1
                d = "LU"
    elif d=="RD":
        if 0<=h+1<9 and 0<=w+1<9:
            w += 1
            h += 1
        else:
            if h+1>=9 and w+1>=9:
                h -= 1
                w -= 1
                d = "LU"
            elif h+1>=9:
                h -= 1
                w += 1
                d = "RU"
            elif w+1>=9:
                h += 1
                w -= 1
                d = "LD"
    elif d=="LU":
        if 0<=h-1<9 and 0<=w-1<9:
            w -= 1
            h -= 1
        else:
            if h-1<0 and w-1<0:
                h += 1
                w += 1
                d = "RD"
            elif h-1<0:
                h += 1
                w -= 1
                d = "LD"
            elif w-1<0:
                h -= 1
                w += 1
                d = "RU"
    elif d=="LD":
        if 0<=h+1<9 and 0<=w-1<9:
            w -= 1
            h += 1
        else:
            if h+1>=9 and w-1<0:
                h -= 1
                w += 1
                d = "RU"
            elif h+1>=9:
                h -= 1
                w -= 1
                d = "LU"
            elif w-1<0:
                h += 1
                w += 1
                d = "RD"

print(ans)