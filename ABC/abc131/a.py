s = input()

pre = s[0]
for i in s[1:]:
    if i==pre:
        print('Bad')
        exit()
    pre = i
print('Good')