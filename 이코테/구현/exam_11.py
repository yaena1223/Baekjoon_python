import sys
from collections import deque
input = sys.stdin.readline

#보드의 크기
n = int(input())

#보드 배열
board = [[0 for i in range(n)] for j in range(n)]

#사과의 개수
k = int(input())

#사과 위치 입력 받고 보드에 표시
apple_location = []
for i in range(k):
    x,y = map(int,input().split())
    board[x-1][y-1] = 1

#뱀의 방향 변환 횟수
l = int(input())

#방향 변환 정보
direction_list = deque([])
for i in range(l):
    x, c = input().split()
    direction_list.append([int(x),c])

#문제 풀이....

#데크
snake_position = deque([])

#뱀 초기 위치
snake_position.append((0,0))

cnt = 0
#방향은 0, 1, 2, 3 (우,하,좌,상)
#D이면 (direction+1)%4
#L이면 (direction-1)%4 단, direction-1이 -1이면 3으로
direction = 0

#우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while True:
    #시간 흘러가는거
    cnt +=1
    # print(snake_position)

    #머리 한칸 앞으로 가는거 (방향에 따라)
    new_x = snake_position[-1][0]+dx[direction]
    new_y = snake_position[-1][1]+dy[direction]

    if new_x <0 or new_y <0 or new_x>=n or new_y>=n:
        break
    if (new_x,new_y) in snake_position:
        break
    snake_position.append((new_x,new_y))


    #머리 이동한 칸에 사과 없으면, 꼬리 없앰
    if board[new_x][new_y] == 0:
        snake_position.popleft()
    else:
        board[new_x][new_y] = 0

    #현재 시간 = 방향 전환 정보의 시간이랑 일치하면 방향 변경
    if direction_list and direction_list[0][0] == cnt:
        x, c = direction_list.popleft()
        if c == "L":
            if direction == 0:
                direction = 3
            else:
                direction = (direction - 1) % 4
        if c == "D":
            direction = (direction+1)%4

print(cnt)