n = int(input())
a, b = map(int, input().split())

if n<=a: print("Takahashi")
else:
    if a==b:
        if n%(a+1)==0: print("Aoki")
        else: print("Takahashi")
    else:
        if a>b: print("Takahashi")
        else: print("Aoki")