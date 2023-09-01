s = list(input())

# 各Wについてそれより左側にあるBの数だけ移動可能
n = 0
ans = 0
for i in range(len(s)):
    if s[i]=='B':
        n += 1
    else:
        ans += n

print(ans)