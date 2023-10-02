n, m = map(int, input().split())
ans_l = [-1] * n

for i in range(m):
    s, c = map(int, input().split())
    if ans_l[s-1] == -1:
        ans_l[s-1] = c
    else:
        if ans_l[s-1] == c:
            continue
        else:
            print(-1)
            exit()

ans = ''
if n>1:
    for i in range(n):
        if ans_l[i] == -1:
            if i != 0:
                ans += '0'
            else:
                ans += '1'
        else:
            ans += str(ans_l[i])
else:
    if ans_l[0]==-1:
        print(0)
        exit()
    else:
        print(ans_l[0])
        exit()

if ans.count('0')==n and n!=1:
    print(-1)
else:
    print(ans)