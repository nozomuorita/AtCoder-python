n = int(input())
s = input()

abc = "b"
cnt = 0
while len(abc)<=110:
    if abc==s:
        exit(print(cnt))
    
    if cnt%3==0:
        abc = "a" + abc + "c"
    elif cnt%3==1:
        abc = "c" + abc + "a"
    else:
        abc = "b" + abc + "b"
    
    cnt += 1

print(-1)