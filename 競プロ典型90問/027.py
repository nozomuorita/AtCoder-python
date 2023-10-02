n = int(input())
usr = set()

for i in range(n):
    s = input()
    if s not in usr:
        print(i+1)
        usr.add(s)