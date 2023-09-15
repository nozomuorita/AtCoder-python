s = input()
t = input()
atcoder = "atcoder"

for i in range(len(s)):
    if s[i] != t[i]:
        if s[i] == "@" and t[i] in atcoder:
            continue
        elif t[i] == "@" and s[i] in atcoder:
            continue
        else:
            print("You will lose")
            exit()
print("You can win")
