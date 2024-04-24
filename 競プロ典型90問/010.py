n = int(input())
cum = [[0, 0]] # [1組の人の累積和, 2組の人の累積和]
for i in range(n):
    c, p = map(int, input().split())
    if c==1:
        cum.append([cum[-1][0]+p, cum[-1][1]])
    else:
        cum.append([cum[-1][0], cum[-1][1]+p])

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    ans1 = cum[r][0] - cum[l-1][0]
    ans2 = cum[r][1] - cum[l-1][1]
    print(ans1, ans2)