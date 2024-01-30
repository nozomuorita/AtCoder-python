s = input()
k = int(input())

word = set()
for i in range(len(s)-k+1):
    word.add(s[i:i+k])

print(len(word))
