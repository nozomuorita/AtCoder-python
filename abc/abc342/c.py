from collections import defaultdict
n = int(input())
s = input()
q = int(input())

d = defaultdict(str)
for i in range(26):
    d[chr(ord("a")+i)] = chr(ord("a")+i)

for _ in range(q):
    C, D = map(str, input().split())

    if d[C]==C: d[C] = D
    for i in range(26):
        ch = chr(ord("a")+i)
        if d[ch]==C:
            d[ch] = D

for i in s:
    print(d[i], end="")