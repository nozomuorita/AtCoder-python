X, Y = map(int, input().split())
if X >= Y:
    print(0)
    exit()

ans = -(-(Y-X) // 10)
print(ans)