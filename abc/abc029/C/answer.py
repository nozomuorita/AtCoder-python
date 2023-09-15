n = int(input())
char = ['a', 'b', 'c']

# 3進数で表し、文字を追加していく
for i in range(3**n):
    s = []
    if i==0:
        s = [char[0]] * n
        print(''.join(reversed(s)))
        continue

    while len(s)!=n:
        if i==0:
            s += char[0]
            continue
        s += char[i%3]
        i //= 3
        
    print(''.join(reversed(s)))