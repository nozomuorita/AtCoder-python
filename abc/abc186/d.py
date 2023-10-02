"""
・ソートした状態で処理をする
・ソートした状態であれば、各jはiよりも大きいことになる
・すなわち、ソート後のものは|Ai-Aj|=Aj-Aiとなる。
・よってi以降(すべてのj)についてsum(Aj)したものから、(jの数)*Aiとすると答えになる
・0<=i<j<=n-1に対して、(A_j - A_i)+(A_j+1 - A_i) + (A_j+2 - A_i) = (A_j + A_j+1 + A_j+2) - 3*A_i
・今回は、順序を考慮しない組み合わせによる最終的な和なのでソートしてから処理しても最終的な結果は変わらない(計算する組み合わせは同じだし、絶対値を計算するためiとjが逆でも結果は同じ)
"""

n = int(input())
a = list(map(int, input().split()))

a.sort()
a_cum = [0]
for i in range(n):
    a_cum.append(a_cum[i] + a[i])
    
ans = 0
for i in range(n):
    ans += (a_cum[-1]-a_cum[i+1]) - (n-(i+1))*a[i]
    
print(ans)