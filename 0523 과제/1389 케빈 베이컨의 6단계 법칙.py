n, m = map(int,input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for i in range(n+1)]


for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
'''for i in range(1,n+1):
    print(graph[i])'''

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
#print()
for i in range(n+1):
    for j in range(n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

'''for i in range(1,n+1):
    print(graph[i])'''

sum_list = []
for i in range(1,n+1):
    sum1 = sum(graph[i])
    sum_list.append(sum1)

sum_list2 = sum_list.copy()
sum_list2.sort()
#print(sum_list)
#print(sum_list2)
ans = 0
for i in range(n):
    if sum_list[i] == sum_list2[0]:
        ans = i+1
        break

print(ans)