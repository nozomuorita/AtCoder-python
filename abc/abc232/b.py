s=list(input())
t=list(input())
s_ord=[]
t_ord=[]

# 文字コードの差分が等しいならYes
for i in range(len(s)):
    s_ord.append(ord(s[i]))
    t_ord.append(ord(t[i]))

dist=[]
for i in range(len(s)):
    tmp=(s_ord[i]-t_ord[i])%26
    dist.append(tmp)

if len(set(dist))==1:
    print('Yes')
else:
    print('No')