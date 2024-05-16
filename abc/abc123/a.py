abcde = [int(input()) for _ in range(5)]
k = int(input())

for i in range(5):
    for j in range(i+1, 5):
        if abs(abcde[i]-abcde[j])>k: exit(print(":("))

print("Yay!")