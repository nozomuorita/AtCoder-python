"""
・hokudaiの文字が登場した時、その文字に到達する通りはその一文字前までの通り数。
・cが出てきたら辞書のcに1インクリメント
・hokudaiが出てきたら、その1文字前の文字の通り分足す(hが出てきたら、その時点であるcの通り数だけパターンがある)。
"""
from collections import defaultdict
mod = 10**9+7
s = list(input())
d = defaultdict(int)

for i in range(len(s)):
    if s[i]=='c':
        d[s[i]] += 1
    elif s[i] in 'hokudai':
        idx = 'chokudai'.index(s[i]) - 1
        d[s[i]] += d['chokudai'[idx]]
    d[s[i]] %= mod
            
print(d['i'])