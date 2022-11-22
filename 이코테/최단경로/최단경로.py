import heapq
import sys
input = sys.stdin.readline
V, E = map(int,input().split())
k = int(input())
INF = int(1e9)
graph = [[] for j in range(V+1)]
distance = [INF]*(V+1)
for i in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

queue = []
heapq.heappush(queue,(0,k))
distance[k] = 0

while queue:
    dist, now = heapq.heappop(queue)
    if distance[now] < dist:
        continue

    for i in graph[now]:
        calc = dist + i[1]
        if calc < distance[i[0]]:
            distance[i[0]] = calc
            heapq.heappush(queue,(calc,i[0]))


for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])