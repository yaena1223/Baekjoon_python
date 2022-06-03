from collections import deque
m, n , h = map(int,input().split())
dm = [0, 0, 0, 0, -1, 1]
dn = [0, 0, 1, -1, 0, 0]
dh = [1, -1, 0, 0, 0, 0]
box = []
tomato = []
for i in range(1,h*n+1):
    line = list(map(int,input().split()))
    tomato.append(line)
    if i%n == 0:
        box.append(tomato)
        tomato = []


#print(box)
visited = [[[0 for i in range(m)]for i in range(n)]for i in range(h)]

first = 0
queue = deque()
for i in range(h):
    for j in range(n):
        for z in range(m):
            if box[i][j][z] == 1:
                visited[i][j][z] = 1
                queue.append([i,j,z])


while queue:
    v = queue.popleft()
    h1 = v[0]
    n1 = v[1]
    m1 = v[2]
    for i in range(6):
        new_h = h1 + dh[i]
        new_n = n1 + dn[i]
        new_m = m1 + dm[i]
        if new_h<0 or new_m<0 or new_n<0 or new_h>=h or new_n>=n or new_m>=m:
            continue

        if box[new_h][new_n][new_m] == 0 and visited[new_h][new_n][new_m] == 0:
            visited[new_h][new_n][new_m] = visited[h1][n1][m1]+1
            box[new_h][new_n][new_m] = 1
            queue.append([new_h, new_n, new_m])

max_num = 0
flag = True
for i in range(h):
    for j in range(n):
        for z in range(m):
            if max_num < visited[i][j][z]:
                max_num = visited[i][j][z]
            if box[i][j][z] == 0:
                flag = False
if flag:
    print(max_num-1)
else:
    print(-1)