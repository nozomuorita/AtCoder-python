h, w, x, y = map(int, input().split())
s = [input() for _ in range(h)]

ans = 1
i, j = x-1, y-1
for d1, d2 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    i2 = i + d1
    j2 = j + d2
    #print(i2, j2, 0)
    if (i2<0) or (i2>(h-1)) or (j2<0) or (j2>(w-1)):
        #print(-1)
        continue
    while (s[i2][j2]!='#'):
        if s[i2][j2]!='#':
            #print(i2, j2)
            ans += 1
            i2 += d1
            j2 += d2
        else:
            break
        if (i2<0) or (i2>(h-1)) or (j2<0) or (j2>(w-1)):
            break

print(ans)