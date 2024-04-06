a, b = map(int, input().split())
if (a>0 and b>0) or (a<0 and b<0):
    print(abs(a-b))
else:
    print(abs(a-b)-1)