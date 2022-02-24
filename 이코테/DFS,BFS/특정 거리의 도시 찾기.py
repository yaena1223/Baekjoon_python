'''
1~n번까지의 도시
m개의 단방향 도로
모든 도로의 거리는 1
도시 x에서 출발하여 도달할 수 있는 모든 도시 중, 최단 거리가 k인 모든 도시의 번호를 출력

<입력>
첫째 줄 : 도시의 개수 n, 도로의 개수 m, 거리 정보 k, 출발 도시의 번호 x
'''
from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph=[[]for i in range(n+1)]
distance = [-1]*(n+1)
distance[x] = 0

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

queue = deque()
queue.append(x)
while queue:
    x = queue.popleft()
    for i in graph[x]:
        if distance[i]==-1:
            distance[i] = distance[x]+1
            queue.append(i)

cnt = 0
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        cnt += 1
if cnt==0:
    print(-1)
