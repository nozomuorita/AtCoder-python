s = input()
t = input()

ans = []
for i in range(len(s)-len(t)+1):
    u = 0
    for j in range(len(t)):
        if s[i+j]!=t[j]:
            u += 1
    ans.append(u)

print(min(ans))