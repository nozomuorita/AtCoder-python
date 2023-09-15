s = input()

s_list = [s]
for i in range(len(s)):
    s = s[1:] + s[0]
    s_list.append(s)

print(min(s_list))
print(max(s_list))