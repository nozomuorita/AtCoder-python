from collections import defaultdict
s = input()
t = input().lower()

d = defaultdict(list)
for i in range(len(s)):
    d[s[i]].append(i)

if t[-1]!="x":
    if len(d[t[0]])==0:
        exit(print('No'))
    else:
        idx = d[t[0]][0]
        if len(d[t[1]])==0:
            exit(print('No'))
        else:
            f = False
            for i in d[t[1]]:
                if i>idx:
                    idx = i
                    f = True
                    break
            if f==False:
                exit(print('No'))
            
            if len(d[t[2]])==0:
                exit(print('No'))
            else:
                f = False
                for i in d[t[2]]:
                    if i>idx:
                        exit(print('Yes'))
                if f==False:
                    exit(print('No'))
else:
    if len(d[t[0]])==0:
        exit(print('No'))
    else:
        idx = d[t[0]][0]
        if len(d[t[1]])==0:
            exit(print('No'))
        else:
            f = False
            for i in d[t[1]]:
                if i>idx:
                    idx = i
                    f = True
                    break
            if f==False:
                exit(print('No'))
            else:
                exit(print('Yes'))
