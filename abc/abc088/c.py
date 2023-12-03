c = [list(map(int, input().split())) for _ in range(3)]

for i in range(101):
    for j in range(101):
        for k in range(101):
            b1 = c[0][0] - i
            b2 = c[0][1] - i
            b3 = c[0][2] - i

            if (0<=b1<=100) and (0<=b2<=100) and (0<=b3<=100):
                f = True            
                if c[1][0]!=b1+j: f=False
                if c[1][1]!=b2+j: f=False
                if c[1][2]!=b3+j: f=False

                if c[2][0]!=b1+k: f=False
                if c[2][1]!=b2+k: f=False
                if c[2][2]!=b3+k: f=False

                if f: exit(print('Yes'))
                
print('No')