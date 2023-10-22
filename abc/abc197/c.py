"""
・長さnの場合、区切る場所は(n-1)通りある。この(n-1)個をbit全探索。
・bitが1なら区切るとして、区切らないならリストに要素を追加していく。
・区切るとき、リストに入っている要素のorをとっていく。
・orをとったもの(最終的なもの)をxor計算用リストに入れていく。
・最後にxorリストに入れたもののxorをとりansを更新
"""
n = int(input())
a = list(map(int, input().split()))
ans = float('inf')

if len(a)==1: print(a[0]); exit()           #  もし、長さが1ならその値が答え

for i in range(1, 2**(n-1)):
    sp = []
    bor = []
    for j in range(n-1):
        sp.append(a[j])                    #  or計算用リストに要素を追加
        if (i>>j) & 1:                     #  1の場合 -> 区切る
            t = sp[0]
            for k in range(1, len(sp)):    #  spに入っている要素のorをとっていく
                t |= sp[k]
            bor.append(t)                  #  xor計算用リストに追加
            sp.clear()                     #  or計算用リストをクリア
    
    sp.append(a[n-1])                      #  最後に、a[-1]の要素を追加して残っている部分をor計算(上のfor文では考慮できないため)
    t = sp[0]
    for k in range(1, len(sp)):
        t|=sp[k]
    bor.append(t)

    xor = bor[0]                           #  xor計算
    for k in range(1, len(bor)):
        xor ^= bor[k]
    ans = min(ans, xor)

print(ans)