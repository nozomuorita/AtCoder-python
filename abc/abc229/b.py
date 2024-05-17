a, b = map(str, input().split())

for i in range(1, min(len(a), len(b))+1):
    if int(a[-i])+int(b[-i])>=10:
        exit(print("Hard"))

print("Easy")