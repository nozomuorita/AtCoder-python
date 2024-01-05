# セグメント木
class segtree:
	# 要素 dat の初期化を行う（最初は全部ゼロ）
	def __init__(self, n):
		self.size = 1
		while self.size < n:
			self.size *= 2
		self.dat = [0] * (self.size * 2)
	
	# クエリ 1 に対する処理
	def update(self, pos, x):
		pos += self.size # pos は 0-indexed なので、A[pos] のみに対応するセルの番号は pos + size
		self.dat[pos] = x
		while pos >= 2:
			pos //= 2
			self.dat[pos] = self.dat[pos * 2] + self.dat[pos * 2 + 1] # 8.8 節から変更した部分
	
	# クエリ 2 に対する処理
	# u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
	def query(self, l, r, a, b, u):
		if r <= a or b <= l:
			return 0 # 8.8 節から変更した部分
		if l <= a and b <= r:
			return self.dat[u]
		m = (a + b) // 2
		answerl = self.query(l, r, a, m, u * 2)
		answerr = self.query(l, r, m, b, u * 2 + 1)
		return answerl + answerr # 8.8 節から変更した部分

n, Q = map(int, input().split())
z = segtree(n)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0]==1:
        pos, x = q[1], q[2]
        z.update(pos-1, x)
    else:
        l, r = q[1]-1, q[2]-1
        ans = z.query(l, r, 0, z.size, 1)
        print(ans)