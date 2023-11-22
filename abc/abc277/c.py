from collections import defaultdict, deque
n = int(input())
ladder = defaultdict(list)
for i in range(n):
    a, b = map(int, input().split())
    ladder[a].append(b)	
    ladder[b].append(a)

q = deque([1])
visited = {1}
while q:
    v = q.popleft()
    for v2 in ladder[v]:
        if v2 not in visited:
            visited.add(v2)
            q.append(v2)

print(max(visited))