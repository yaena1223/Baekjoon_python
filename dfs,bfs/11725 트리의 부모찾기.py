from collections import deque
n = int(input())
graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0]*(n+1)
queue = deque([1])
visited = [0]*(n+1)
while queue:

    v = queue.pop()
    for i in graph[v]:

        if visited[i] == False:
            visited[i] = True
            queue.append(i)
            ans[i] = v


for i in range(2,n+1):
    print(ans[i])