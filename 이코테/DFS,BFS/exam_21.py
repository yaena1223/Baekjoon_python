from collections import deque

n, l, r = map(int, input().split())
people_cnt = []

for i in range(n):
    temp = list(map(int, input().split()))
    people_cnt.append(temp)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    union = [(x, y)]
    visited[x][y] = 1

    while queue:
        # print(queue)
        x, y = queue.popleft()
        # print(queue)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:
                continue
            elif l <= abs(people_cnt[new_x][new_y] - people_cnt[x][y]) <= r and not visited[new_x][new_y]:
                union.append((new_x, new_y))
                queue.append((new_x, new_y))
                visited[new_x][new_y] = 1

    if len(union) == 1:
        return False
    else:
        move = 0
        for a, b in union:
            move += people_cnt[a][b]
        move = move // len(union)

        for a, b in union:
            people_cnt[a][b] = move

        return True
    return True


day = 0
# 날짜 카운트
while True:
    visited_cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                visited_cnt += 1
            # print(people_cnt)
    if visited_cnt == n * n:
        break
    day += 1

print(day)