n, m = map(int, input().split())
s = input()

ans = 0
muji, rogo = m, 0
for i in s:
    if i=="0":
        rogo = ans
        muji = m
    elif i=="1":
        if muji>0: muji-=1
        else:
            if rogo>0:
                rogo -= 1
            else:
                ans += 1
    else:
        if rogo>0: rogo-=1
        else:
            ans += 1

print(ans)