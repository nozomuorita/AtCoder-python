s = list(input())
n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    tmp = list(reversed(s[l: r+1]))
    print(tmp)

    for j, k in enumerate(range(l, r+1)):
        print(j, k)
        s[k] = tmp[j]

print(''.join(s))