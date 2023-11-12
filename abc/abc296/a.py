N = int(input())
S = input()
flag = True

for i in range(1, len(S)):
    if S[i] == S[i-1]:
        flag = False
        break

if len(S)==1:
    flag = True
    
if flag:
    print('Yes')
else:
    print('No')