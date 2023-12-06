x, y = map(int, input().split())
ans = float("inf")

# pattern1: 押さない→押さない
if y>=x: score=y-x; ans=min(ans, score)

# pattern2: 押す→押さない
v, score = -x, 1
if v<=y: score+=y-v; ans=min(ans, score)

# pattern3: 押さない→押す
v, score = x, 0
if v<=-y: score+=abs(-y-v)+1; ans=min(ans, score)

# pattern4: 押す→押す
v, score = -x, 1
if v<=-y: score+=abs(-y-v)+1; ans=min(ans, score)

print(ans)