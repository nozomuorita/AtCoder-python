n = input()
score = 0
for i in n:
    score += int(i)

print('Yes') if score%9==0 else print('No')