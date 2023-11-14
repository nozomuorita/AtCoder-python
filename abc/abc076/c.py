"""
・tを埋め込むことのできる一番後ろの場所を探す
・見つけたら、そこに埋め込み、他の？はaで埋める
・埋め込める場所が見つからなかったら、UNRESTORABLE
"""
s = input()
t = input()

idx = -1
for i in range(len(s)):
    if s[i]==t[0] or s[i]=='?':
        tmp = i
        if (i+len(t)-1)>=len(s): continue
        for j in range(len(t)):
            if s[tmp+j]==t[j] or s[tmp+j]=='?': continue
            else: break
        else:
            idx = i

if idx==-1: exit(print('UNRESTORABLE'))
else:
    ans = ""
    for i in range(len(s)):
        if idx<=i<(idx+len(t)): ans+=t[i-idx]
        else:
            if s[i]=="?": ans+="a"
            else: ans+=s[i]

print(ans)