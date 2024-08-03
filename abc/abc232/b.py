s = input()
t = input()

s2 = [ord(i)-ord("a") for i in s]
t2 = [ord(i)-ord("a") for i in t]

dist = []
for i in range(len(s)):
    dist.append(((t2[i]+26)-s2[i])%26)

print('Yes') if len(set(dist))==1 else print('No')