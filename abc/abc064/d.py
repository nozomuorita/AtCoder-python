n = int(input())
s = input()

mn, cur = float("inf"), 0
op = 0
for i in s:
    if i=="(":
        cur += 1
        op += 1
    else:
        cur -= 1
        if op>0: op-=1
    mn = min(mn, cur)

s = ("(" * max(-mn, 0)) + s + (")" * op)
print(s)