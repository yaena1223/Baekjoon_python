# 1*1 크기의 정사각형으로 이루어
# a는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸으 ㅣ개수
# 바다에는 갈 수 X
# 왼쪽칸에 아직 안가본 칸 있으면 왼쪽으로 회전해서 전진, 없으면 왼쪽으로 회전만

n, m = map(int, input().split())
map1 = []
visited = [[0]*m for j in range(n)]
# print(map1)
x, y, d = map(int, input().split())  # x, y는 현위치 좌표값, d는 바라보는 방향(북동남서 순)
visited[x][y] = 1
for i in range(n):
    l = list(map(int, input().split()))
    map1.append(l)
#print(map1)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 1


def turn_left(): # d = 0 이면 왼쪽으로 돌면 d = 3, d = 1이면 왼쪽으로 돌면 d = 0, d = 2 -> d = 1, d=3->d=2
    global d
    d -= 1
    if d == -1:
        d = 3


turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if map1[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        ans += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if map1[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(ans)