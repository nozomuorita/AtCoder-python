S = input()

s = '0123456789'

for i in s:
  if i not in S:
    print(i)
    exit()