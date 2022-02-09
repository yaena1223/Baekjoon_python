n = int(input())
e = int(input())
graph_list = [[] for i in range(n + 1)]
for i in range(e):
    a, b = map(int, input().split())
    graph_list[a].append(b)
    graph_list[b].append(a)
visit = [False for i in range(n + 1)]


def dfs(graph, visited, v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)


cnt = 0
dfs(graph_list, visit, 1)
print(visit)
for i in visit:
    if i:
        cnt+=1

print(cnt-1)