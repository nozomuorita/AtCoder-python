h = int(input())
height = 0
ans = 0

while 1:
    height += 2**ans
    ans += 1
    if height>h:
        exit(print(ans))