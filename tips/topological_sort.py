from collections import deque
def topological_sort(n, G, into_num):
    """
    トポロジカルソート

    Args:
        n (int): 頂点数
        G (list 2d): 隣接リスト
        into_num (list): 入次数

    Returns:
        ans(list): トポロジカル順序
    """
    #入ってくる有向辺を持たないノードを列挙
    q = deque()
    #V: 頂点数
    for i in range(n):
        if into_num[i]==0:
            q.append(i)
    
    #以下、幅優先探索
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1 #入次数を減らす
            if into_num[adj]==0:
                q.append(adj) #入次数が0になったら、キューに入れる
    
    return ans

#  閉路確認
# ans = topological_sort(G, into_num) #トポロジカルソート
# #トポロジカルソートされたリストの頂点数　と　元のグラフの頂点数を比較
# if len(ans)==len(G):
#     print('閉路なし') #同じ頂点数なら閉路なし
# else:
#     print('閉路有り') #頂点数が異なると閉路が存在している