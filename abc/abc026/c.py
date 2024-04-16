n = int(input())
ans = [1]*n
under = [[] for _ in range(n)]

for i in range(1, n):
    b = int(input()) - 1
    under[b].append(i)

for i in reversed(range(n)):
    money = []
    for j in under[i]:
        money.append(ans[j])
    if len(money)==0: continue
    ans[i] = max(money) + min(money) + 1

print(ans[0])