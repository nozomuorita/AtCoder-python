s = []
for i in range(8):
    tmp = input()
    s.append(tmp)
    
for i in range(8):
    for j in range(8):
        if s[i][j]=='*':
            a = i
            b = j
            break
            
a1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a2 = [8, 7, 6, 5, 4, 3, 2, 1, 0]

ans = a1[b] + str(a2[a])
print(ans)