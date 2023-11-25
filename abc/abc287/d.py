"""
・sの先頭からx文字がマッチしているか
・sの末尾x文字がマッチしているかをそれぞれ事前計算
・各xについて、先頭x文字がマッチかつ、末尾len(t)-x文字がマッチでyesと判定できる
"""
s = input()
t = input()

head, tail = [True]+[False]*(len(t)), [True]+[False]*len(t)
#  先頭からのマッチを見る
for i in range(len(t)):
    if s[i]==t[i] or s[i]=="?" or t[i]=="?": head[i+1]=True
    else: break
        
#  後ろからのマッチを見る
for i in range(1, len(t)+1):
    if s[-i]==t[-i] or s[-i]=="?" or t[-i]=="?": tail[i]=True
    else: break

for i in range(len(t)+1):
    print('Yes') if head[i] and tail[len(t)-i] else print('No')