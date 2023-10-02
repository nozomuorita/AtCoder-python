"""
・全パターンから該当するものを引く
・考えられる全パターン(3つの文字がすべて異なるもの)は「Rの個数」 * 「Gの個数」 * 「Bの個数」である
・ここからiとjをfor文で回し、固定して一つずつ調べる(iとjを決定すると「j-i == k-j」であるものが一意に定まる)
・「j-i == k-j」を満たすものについて、すべての文字が異なるなら1引く
"""

n = int(input())
s = input()
r = s.count('R')
g = s.count('G')
b = s.count('B')
ans = r*g*b  # 全パターン

# i, jを決定して全探索
for i in range(n-2):
    for j in range(i+1,n-1):
        k = -i +2*j
        # i, jを固定した時のkを計算し、jよりも小さいか範囲外の場合はbreak
        if k > n-1 or k <=j :
            break
        if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
            ans -= 1
print(ans)