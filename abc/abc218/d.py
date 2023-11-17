from collections import defaultdict
n = int(input())

# key: x座標、value: y座標(list)
d = defaultdict(list)
for i in range(n):
    x, y = map(int, input().split())
    d[x].append(y)
    
ans = 0
keys = list(d.keys())
# dからx座標を2つ選択(2重ループ)
for i in range(len(keys)):
    if len(d[keys[i]])<2: continue         #  x座標がkeys[i]である点が2つ未満なら不可なのでcontinue
    for j in range(i+1, len(keys)):
        if len(d[keys[j]])<2: continue     #  x座標がkeys[j]である点が2つ未満なら不可なのでcontinue
        
        #  x座標がkeys[i]である点からy座標を2つ選択(2重ループ)
        for k in range(len(d[keys[i]])):
            for l in range(k+1, len(d[keys[i]])):
                if d[keys[i]][k]==d[keys[i]][l]: continue      #  取り出しだ2点のy座標が等しいなら同じ点を選択しており、これは不可なのでcontinue
                if (d[keys[i]][k] in d[keys[j]]) and (d[keys[i]][l] in d[keys[j]]): ans+=1    #  選択した2点のy座標がkeys[j]のほうにもあればok
                
print(ans)