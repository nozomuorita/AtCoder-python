n = int(input())
f = [1]
for i in range(10):
    f.append(f[-1]*(i+1))

print(f[n])