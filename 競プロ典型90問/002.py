# 長さが20なのでbit全探索する
n = int(input())

ans = []
for i in range(2**n):
    s = ""
    t = 0
    for j in range(n):
        if (i>>j) & 1:
            s += "("
            t += 1
        else:
            s += ")"
            t += -1
            
        if t < 0:
            break
    if t==0:
        ans.append(s)
        
for i in sorted(ans):
    print(i)