a, b = map(int, input().split())
if a==b: print("Draw")
else:
    if a==1 or b==1:
        print("Alice") if a==1 else print("Bob")
    else:
        print("Alice") if a>b else print("Bob")