s = list(input())
s.insert(0, "0")
for i in range(1, len(s)//2+1):
    s[2*i-1], s[2*i] = s[2*i], s[2*i-1]
print("".join(s[1:]))