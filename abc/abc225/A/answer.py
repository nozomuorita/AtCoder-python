S = list(input())

S_set = set(S)

if len(S_set)==3:
    print(6)
elif len(S_set)==2:
    print(3)
else:
    print(1)