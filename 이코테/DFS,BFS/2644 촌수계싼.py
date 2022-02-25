n = int(input())
a, b = map(int,input().split())
m = int(input())
graph=[[]for i in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visited=[0]*(n+1)
from collections import deque
def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i]==0:
                visited[i] = visited[a] + 1
                queue.append(i)


bfs(a)
ans = visited[b]
print(ans if ans>0 else -1)
