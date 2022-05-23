INF = int(1e9)
n = int(input())
graph = []
for i in range(n):
    a = list(map(int,input().split()))
    graph.append(a)

for i in range(n):
    for j in range(n):
        if graph[i][j]==0:
            graph[i][j] = INF
#print(graph)
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j]>=1 and graph[i][j]!=INF:
            graph[i][j] = 1
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(n):
    print(*graph[i])