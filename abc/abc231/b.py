n = int(input())
s = [input() for _ in range(n)]
s_set = set(s)

mx = -1

for i in s_set:
    num = s.count(i)
    if num > mx:
        ans = i
        mx = num

print(ans)