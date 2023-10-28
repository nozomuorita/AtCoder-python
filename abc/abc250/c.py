"""
各ボールをリストbollで管理
各ボールのインデックス番号をidxで管理
pythonのため、すべての数字をマイナス1して計算

入力例１の場合、
boll = [0, 1, 2, 3, 4, 5] 一番左端には0と書かれたボールがあり、その右には、1と書かれたボールがある
idx = [0, 1, 2, 3, 4, 5] idx[0]は0と書かれたボールがあるインデックス番号、idx[1]には1と書かれたボールがあるインデックス番号

x = 1 - 1 = 0が入力される
→0と書かれたボールを右のものと交換
boll = [1, 0, 2, 3, 4, 5] ボールを交換するため、0と1を交換
idx = [1, 0, 2, 3, 4, 5] # 0と書かれたボールが右へ行き、1と書かれたボールが左へ行くためidx[0]はプラス１され、idx[1]はマイナス１される

これを繰り返すことでO(q)で処理可能
"""

from collections import defaultdict
n, q = map(int, input().split())
d = defaultdict(int)
for i in range(n+1): d[i] = i
b = [i for i in range(n+1)]

for _ in range(q):
    x = int(input())
    idx = b[x]
    if idx!=n:
        left = d[idx]
        right = d[idx+1]
        
        b[left], b[right] = b[right], b[left]
        d[idx], d[idx+1] = right, left
    else:
        left = d[idx]
        right = d[idx-1]
        
        b[left], b[right] = b[right], b[left]
        d[idx], d[idx-1] = right, left

ans = []
for i in range(1, n+1): ans.append(d[i])
print(*ans)