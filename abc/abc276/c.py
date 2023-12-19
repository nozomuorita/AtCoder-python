"""
・後ろから見て、数が大きくなるところまで見ていく
・大きくなっているところの数xをそれまでに登場した数字の中でxより小さく、最も大きいものに置き換える
・以降を、xと入れ替えたもの以外で降順に並べる
・手前側はそのまま
"""
n = int(input())
p = list(map(int, input().split()))

lst = [p[-1]]
ans = []
for i in range(n-2, -1, -1):
    if p[i]<lst[-1]: lst.append(p[i])
    else:
        mn = -1
        for j in range(len(lst)):
            if p[i]>lst[j]: mn=lst[j]; break
        ans.append(mn)
        lst.remove(mn)
        lst.append(p[i])
        break
    
ans += sorted(lst, reverse=True)
ans = p[:i] + ans
print(*ans)