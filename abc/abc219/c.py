"""
・各名前を新しいアルファベット順に倣って、作り変え、それをkeyとして辞書に追加
・keyをソートし、値(元の名前)を出力
"""
from collections import defaultdict
x = input()
n = int(input())

alphabet = [chr(ord('a')+i) for i in range(26)]
d = defaultdict(str)

for _ in range(n):
    s = input()
    name = []
    for i in s:
        name.append(alphabet[x.index(i)])
    name = "".join(name)
    d[name] = s
    
keys = sorted(d.keys())
for key in keys: print(d[key])