"""
・愚直に判定
"""
n, t = map(str, input().split())
n = int(n)
s = [input() for _ in range(n)]

ans = 0
ans2 = []

for i in range(n):
    # パターン1
    if s[i]==t:
        ans += 1
        ans2.append(i+1)
        continue
    
    # パターン4
    # 長さが異なる場合、異なる文字が1つならOK
    if len(s[i])==len(t):
        diff = 0
        f = True
        for j in range(len(t)):
            if s[i][j]==t[j]: continue
            else:
                diff += 1
            if diff>=2:
                f = False
                break
        if f:
            ans += 1
            ans2.append(i+1)
            
    # パターン2
    # 長さの差が1であれば通る
    # 異なる文字が一つあれば、インデックスを一つずらす
    elif len(s[i])>len(t) and (len(s[i])-len(t)==1):
        tmp = 0
        f = True
        for j in range(len(t)):
            if s[i][j+tmp]==t[j]: continue
            else:
                if tmp==0:
                    tmp += 1
                    if s[i][j+tmp]==t[j]: continue
                    else:
                        f = False
                        break
                else:
                    f = False
                    break
        if f:
            ans += 1
            ans2.append(i+1)
            
    # パターン3
    # パターン2の逆バージョン
    elif len(s[i])<len(t) and (len(t)-len(s[i])==1):
        tmp = 0
        f = True
        for j in range(len(s[i])):
            if s[i][j]==t[j+tmp]: continue
            else:
                if tmp==0:
                    tmp += 1
                    if s[i][j]==t[j+tmp]: continue
                    else:
                        f = False
                        break
                else:
                    f = False
                    break
        if f:
            ans += 1
            ans2.append(i+1)

print(ans)
print(*ans2)