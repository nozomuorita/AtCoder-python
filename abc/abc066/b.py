s = input()
for i in range(1, len(s)):
    s2 = s[:-i]
    if len(s2)%2!=0: continue
    if s2[:len(s2)//2]==s2[len(s2)//2:]:
        exit(print(len(s2)))