s = list(input())

s_alphabet = set()
alphabet = []
for i in range(26):
    s_ = chr(ord('a') + i)
    alphabet.append(s_)

for i in s:
    s_alphabet.add(i)
    
ans = ''
for i in alphabet:
    if i not in s_alphabet:
        ans += i
        break
    
print(ans if len(ans)==1 else 'None')