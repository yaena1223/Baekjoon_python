n, m = map(int,input().split())
a, b, d= map(int,input().split())

visited = [[0 for i in range(m)] for j in range(n)]

lo_list = []
for i in range(n):
    li = list(map(int,input().split()))
    lo_list.append(li)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1

print(lo_list)
visited[a][b] = 1
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

ans = 1
while True:
    turn_left()

    new_a = a + dx[d]
    new_b = b + dy[d]

    if new_a <0 or new_b <0 or new_a >=n or new_b>=m:
        continue

    if visited[new_a][new_b] == 0 and  lo_list[new_a][new_b] == 0:
        visited[new_a][new_b] =1
        # print(new_a, new_b)
        a, b = new_a,new_b
        ans += 1
        cnt = 0

    else:
        cnt += 1

    if cnt == 4:
        new_a = a - dx[d]
        new_b = b - dy[d]
        if lo_list[new_a][new_b] == 0:
            a, b = new_a, new_b
        else:
            break
        cnt = 0

print(ans)