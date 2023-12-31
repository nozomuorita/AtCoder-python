from sortedcontainers import SortedList
n, k, q = map(int, input().split())
big = SortedList([0]*k)                       # 大きいほうからk個
sml = SortedList([0]*(n-k))                   # それ以外のn-k個
s = 0                                         # 大きいほうからk個の和
lst = [0]*n                                   # 各要素の値
ans = []
for _ in range(q):
    x, y = map(int, input().split())
    x -= 1
    # n==k(全要素の和)の場合→x番目の要素を取り除き、新たにyを追加
    if n==k:
        big.discard(lst[x])
        big.add(y)
        s -= lst[x]
        s += y
        lst[x] = y
    else:
        # yがbigの中の最小値よりも大きい場合→bigに入れる場合
        if big[0]<=y:
            # lst[x](変更するもの)がすでにbigに入っている場合→bigにあるlst[x]を書き換える
            if big[0]<=lst[x]:
                big.discard(lst[x])
                big.add(y)
                s -= lst[x]
                s += y
                lst[x] = y
            # lst[x](変更するもの)がbigに入っていない場合→bigの最小値をsmlに移し、smlにあるlst[x]をyにしてbigに移す
            else:
                v = big.pop(0)
                big.add(y)
                sml.discard(lst[x])
                sml.add(v)
                s -= v
                s += y
                lst[x] = y
        # yがbigの最小値よりも小さい場合(bigに入らない場合)
        else:
            # lst[x]がbigに入っている場合→bigからlst[x]を取り除き、smlに追加し、smlの最大値をbigに移動
            if big[0]<=lst[x]:
                v = sml.pop()
                # smlの最大値よりもyが大きいなら、yをbigに入れる
                if v<=y:
                    big.discard(lst[x])
                    big.add(y)
                    sml.add(v)
                    s -= lst[x]
                    s += y
                # smlの最大値がyよりも大きい→smlの最大値をbigに入れ、yをsmlに入れる
                else:
                    big.discard(lst[x])
                    big.add(v)
                    sml.add(y)
                    s -= lst[x]
                    s += v                    
                lst[x] = y
            # lst[x]がbigに入っていない場合→smlのlst[x]を書き換える
            else:
                sml.discard(lst[x])
                sml.add(y)
                lst[x] = y
    
    #print(s)
    ans.append(s)

print(*ans)