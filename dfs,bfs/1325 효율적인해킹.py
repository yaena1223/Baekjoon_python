from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
#A가 B를 신뢰하면, B를 해킹했을때 A도 해킹할 수 있음
graph = [[] for i in range(n+1)]


for i in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)

def bfs(x):
    queue = deque([x])
    visited = [0] * (n + 1)
    visited[x] = True
    while queue:
        v = queue.pop()
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

    ans = visited.count(1)
    return ans


list1 = []
max_num = 0
for i in range(1,n+1):
    b = bfs(i)
    if b>max_num:
        list1.clear()
        list1.append(i)
        max_num = b
    elif b==max_num:
        list1.append(i)

list1.sort()
print(*list1)