#1~n번까지의 도시와 mr개의 단방향 도로
#모든 도로의 거리는 1
#특정 도시 X에서 출발하여, 도달할 수 있는 모든 도시 중, 최단거리가 K인 모든 도시의 번호 출렭
from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
# print(graph)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

queue = deque([x])
visited = [0 for i in range(n+1)]
# print(visited)
while(queue):
    pop = queue.popleft()
    for i in graph[pop]:
        if visited[i] == 0:
            visited[i] = visited[pop]+1
            queue.append(i)

visited[x] = 0

if k not in visited:
    print(-1)
else:
    for i in range(1,n+1):
        if visited[i] == k:
            print(i)

