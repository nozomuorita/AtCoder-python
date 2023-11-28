n = int(input())
z = []
for i in range(1, 10**6):
    if len(set(list(str(i))))==1: z.append(i)
    if len(z)>=50: break

print(z[n-1])