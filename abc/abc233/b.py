l, r = map(int, input().split())
s = list(input())

l -= 1
r -= 1

s1 = s[:l]
s2 = s[l: r+1]
s3 = s[r+1:]
s2 = s2[: : -1]
ans = s1 + s2 + s3
#print(s1, s2, s3)
print(''.join(ans))