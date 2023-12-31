s = input()
k = int(input())

subs = set()
for i in range(len(s)):
    for j in range(1, 6):
        subs.add(s[i:i+j])

subs = sorted(list(subs))
print(subs[k-1])