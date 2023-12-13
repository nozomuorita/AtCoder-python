k, g, m = map(int, input().split())

glass, magcup = 0, 0
for i in range(k):
    if glass==g: glass=0
    elif magcup==0: magcup=m
    else:
        if magcup<=g-glass: glass+=magcup; magcup=0
        else:
            d = (g-glass)
            glass = g
            magcup -= d
    
print(glass, magcup)