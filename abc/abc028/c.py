n = list(map(int, input().split()))
sum_list = []

for i in range(len(n)):
    for j in range(i+1, len(n)):
        for k in range(j+1, len(n)):
            s = n[i] + n[j] + n[k]
            sum_list.append(s)
            
sum_list = list(set(sum_list))
sum_list.sort(reverse=True)

print(sum_list[2])