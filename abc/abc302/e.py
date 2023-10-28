"""
・隣接リストをset型で管理する
・set型のremoveでvつながっている頂点からvを削除 → vを削除したときに辺の数が0になるかどうか判定
・vは辺の数が0になる
・削除はdiscardでもよい(discardは存在しない要素へのアクセスでエラーが出ない(今回はどちらでも問題ない))
"""
n, Q = map(int, input().split())
g = [set() for _ in range(n)]
ans = n                                            #  辺がない頂点数(最初はすべて)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0]==1:
        u, v = q[1]-1, q[2]-1
        if len(g[u])==0: ans-=1                    #  頂点uの辺の数が0ならば、今からvとつなぐことで辺を持つようになるのでans-=1
        if len(g[v])==0: ans-=1                    #  同様(すでに辺を持っているならansは変わらない)
        g[u].add(v)                                #  隣接リストに追加
        g[v].add(u)
    
    else:
        v = q[1]-1
        if len(g[v])==0: print(ans); continue      #  頂点vが辺を持っていないなら操作することはないため、ansを出力してcontinue
        ans += 1                                   #  頂点vが辺を持たなくなるため、ans+=1する
        for i in g[v]:                             #  頂点vとつながっている頂点をループで回す
            if len(g[i])==1: ans+=1                #  辺の数が1ならその辺はvとつながっている → 削除して辺の数0になるためans+=1
            g[i].remove(v)                         #  頂点iからvをremove
        g[v] = set()                               #  頂点vの辺はすべて削除するので空のsetにする
    
    print(ans)