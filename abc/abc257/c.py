from collections import defaultdict
n = int(input())
s = input()
w = list(map(int, input().split()))

data = defaultdict(lambda: [0, 0])
for i in range(n):
    if s[i]=="0":
        data[w[i]][0] += 1
    else:
        data[w[i]][1] += 1

cor = s.count("1")
ans = s.count("1")
for key in sorted(list(data.keys())):
    cor += data[key][0]
    cor -= data[key][1]
    
    ans = max(ans, cor)

print(ans)