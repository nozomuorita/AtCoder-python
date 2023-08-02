# 前半と公判を何回入れ替えたかを数えておく
# no submit

n = int(input())
s = input()
q = int(input())
s_list = []

for i in range(len(s)):
    s_list.append([i, s[i]])

f = False # 前後半を入れ替えるか

for i in range(q):
    t, a, b = map(int, input().split())

    if t == 1:
        a -= 1
        b -= 1
        s_list[a][1], s_list[b][1] = s_list[b][1], s_list[a][1]

    else:
        f = not(f)

if f:
    ans = ''
    for i in range(n, 2*n):
        ans += s_list[i][1]

    for i in range(n):
        ans += s_list[i][1]
else:
    ans = ''
    for i in range(n):
        ans += s_list[i][1]

    for i in range(n, 2*n):
        ans += s_list[i][1]

print(ans)
   
