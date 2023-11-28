n, k = map(int, input().split())
ans = ""
num = 0

for i in input():
    if i=="o" and num<k: ans+="o"; num+=1
    else: ans+="x"
print(ans)