from math import comb, factorial

s = list(input())
list1, list2 = [], []
for i in range(len(s)):
    if s[i] == 'o':
        list1.append(i)
    if s[i] == 'x':
        list2.append(i)    

ans = 0
for i in range(10000):
    list3 = [False] * 10
    f = True
    number = str(i).zfill(4)

    for j in number:
        list3[int(j)] = True
        
    for j in list1:
        if list3[j]:
            continue
        else:
            f = False
            break
    
    for j in list2:
        if list3[j]:
            f = False
            break
    
    if f:
        ans += 1

print(ans)
        