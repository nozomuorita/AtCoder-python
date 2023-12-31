n = int(input())
s = list(input())

f = False
for i in range(n):
    if s[i]=='"': f=not(f)
    elif s[i]=="," and not(f): s[i]="."

print("".join(s))