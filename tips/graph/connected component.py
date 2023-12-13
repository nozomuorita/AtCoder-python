# Find the number of connected components by DFS

import sys
sys.setrecursionlimit(10**8)

def connected_components(g, visited, n):
    """
    g: adjacency list
    visited: List to keep track of whether it has been visited or not
    n: number of vertices
    """

    def dfs(i):
        visited[i] = True
        
        for i2 in g[i]:
            if not(visited[i2]):
                dfs(i2)

    num = 0
    for k in range(n):
        if visited[k]:
            continue
        else:
            num += 1
            dfs(k)

    return num

# execution (e.g. program)
n = 5
m = 3
g = [[]]