from collections import deque
n = int(input())
graph = []
for i in range(n):
    graph.append(list(input()))
visited = [[0 for i in range(n)]for j in range(n)]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited[x][y]= 1
    while queue:
        i,j = queue.popleft()
        for z in range(4):
            nx = i + dx[z]
            ny = j + dy[z]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if visited[nx][ny]==1:
                continue
            elif graph[i][j]==graph[nx][ny]:
                visited[nx][ny]=1
                queue.append((nx,ny))
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            bfs(i,j)
            cnt=cnt+1

for i in range(n):
    for j in range(n):
        if graph[i][j]=='R':
            graph[i][j]='G'

cnt2 = 0
visited = [[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            bfs(i,j)
            cnt2=cnt2+1
print(cnt,end=" ")
print(cnt2)