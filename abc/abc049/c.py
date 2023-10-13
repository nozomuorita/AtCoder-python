import sys
sys.setrecursionlimit(100000000)
s = input()

words = ['dream', 'dreamer', 'erase', 'eraser']
words = [i[::-1] for i in words]

word = ''
for i in s[::-1]:
    word += i
    if word in words:
        word = ''

print('YES') if len(word)==0 else print('NO')