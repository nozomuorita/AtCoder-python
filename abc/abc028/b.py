s = list(input())

alphabet = [chr(i) for i in range(ord('A'), ord('F')+1)]
ans = []
for i in alphabet:
    ans.append(s.count(i))
    
print(*ans)