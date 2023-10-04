s = list(input())
for i in range(len(s)):
    if (i%2==0):
        if (s[i]=="R") or (s[i]=="U") or (s[i]=="D"):
            continue
        else:
            print("No")
            exit()
    else:
        if (s[i]=="L") or (s[i]=="U") or (s[i]=="D"):
            continue
        else:
            print("No")
            exit()
print("Yes")