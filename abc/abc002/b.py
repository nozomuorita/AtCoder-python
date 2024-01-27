w = input()
ans = ''

boin = 'aiueo'

for i in w:
    if i in boin:
        continue
    else:
        ans += i

print(ans)