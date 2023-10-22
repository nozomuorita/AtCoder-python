s = list(input())
s = s[: : -1]

ans = ''

for i in s:
    if i == '6':
        ans += '9'
    elif i == '9':
        ans += '6'
    else:
        ans += i

print(ans)