q = int(input())
a = []

for i in range(q):
    t, x = map(int, input().split())
    if t==1:
        a.insert(0, x)
    elif t==2:
        a.append(x)
    else:
        print(a[x-1])

# Q = int(input())
# a = []
# b = []
# for i in range(Q):
#     t,x = map(int,input().split())
#     if t == 1:
#         a.append(x)
#     elif t == 2:
#         b.append(x)
#     elif t == 3:
#         if x <= len(a):
#             print(a[-x])
#         else:
#             x -= len(a)
#             print(b[x-1])