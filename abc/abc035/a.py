w, h = map(int, input().split())

if h == w*(3/4):
    print('4:3')
else:
    print('16:9')