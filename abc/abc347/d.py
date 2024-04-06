a, b, C = map(int, input().split())
one_count = bin(C).count("1")
C_len = len(bin(C)[2:])

f = False
for i in range(one_count+1):
    tmp1, tmp2 = a-i, b-(one_count-i)
    if tmp1==tmp2:
        f=True
        break

if f==False: exit(print(-1))

o = one_count - i
ans1, ans2 = 0, 0
tmp = tmp1

cnt = 0
for j in range(C_len):
    if not((C>>j & 1)) and tmp>0:
        ans1 += 1<<j
        ans2 += 1<<j
        tmp -= 1
    elif cnt<o and (C>>j & 1):
        ans2 += 1<<j
        cnt += 1
    else:
        if (C>>j & 1):
            ans1 += 1<<j

for j in range(C_len, C_len+tmp):
    ans1 += 1<<j
    ans2 += 1<<j

if (bin(ans1).count("1")!=a) or (bin(ans2).count('1')!=b): exit(print(-1))
if (ans1^ans2)!=C: exit(print(-1))

if (len(bin(ans1))-2)>60 or (len(bin(ans2))-2)>60:
    exit(print(-1))

print(ans1, ans2)
