h, w = map(int, input().split())

print("#"*(w+2))
for _ in range(h):
    i = input()
    print("#" + i + "#")
print("#"*(w+2))