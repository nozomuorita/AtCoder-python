s = input()
for i in range(3):
    if s.count(s[i])==1:
        exit(print(s[i]))
print(-1)