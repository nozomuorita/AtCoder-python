S = input()
T = input()

flag = True
n = 0

for i in range(len(T)):
    #print(i)
    if (i >= len(S)):
        if (i-n) < len(S):
            if S[i-n] == T[i]:
                continue
            
            elif (T[i] == S[i-n-1]) and (T[i] == S[i-n-2]):
                n += 1
            else:
                flag = False
                break
        else:
            if (S[i-n-1]==T[i]) and (S[i-n-2]==T[i]):
                n += 1
            else:
                flag = False
                break
         
    else:
        if S[i-n] == T[i]:
            continue
        else:
            if (i >= 2) and (S[i-n-1]==T[i]) and (S[i-n-2]==T[i]):
                n += 1
            else:
                flag = False
                break
        
if flag:
    print('Yes')
else:
    print('No')