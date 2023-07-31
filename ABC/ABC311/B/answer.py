n, d = map(int, input().split())
s = []
for i in range(n):
    s_ = input()
    s.append(s_)
    
ans = []
num = 0

for i in range(d):
    tmp = [j[i] for j in s] # i日目の全員の予定
    #print(tmp)
    if tmp.count('o')==n:
        num += 1
    else:
        ans.append(num)
        num = 0
        
ans.append(num)
        
print(max(ans))