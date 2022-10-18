# 선생님은 상하좌우로 감시 진행
# 장애물이 있으면, 장애물 뒤에 있는 학생은 볼 수 없음
# 장애물 막히기 전까진 다 볼 수 있음
# 선생님 T 학생 S 장애물 O 빈칸 X
# 장애물을 3개 설치하여 모든 학생들이 감시를 피할 수 있게 할 수 있는지 => 출력값 : YES/NO

from collections import deque
import itertools
import copy

#선생님 감시
def bfs(a,b,arr, dir):
    #dir는 상하좌우 (0이면 상 1 : 하 2 :좌 3: 우)
    if dir == 0: #상이면 y좌표 같고 x좌표 작은 곳은 다 볼 수 있음(장애물 없을 경우)
        while(a>=0):
            if arr[a][b] == "O":
                return False
            if arr[a][b] == "S":
                return True
            a -= 1

    if dir == 1: #하이면 y좌표 같고, x좌표 큰 곳은 다 볼 수 있음
        while(a<n):
            if arr[a][b] == "O":
                return False
            if arr[a][b] == "S":
                return True
            a += 1

    if dir == 2: #좌면 x좌표 같고, y좌표 작은 곳
        while(b>=0):
            if arr[a][b] == "O":
                return False
            if arr[a][b] == "S":
                return True
            b-=1

    if dir == 3:#우면 x좌교 같고, y좌표 큰 곳
        while(b<n):
            if arr[a][b] == "O":
                return False
            if arr[a][b] == "S":
                return True
            b +=1


    return False

#입력값 받기
n = int(input())
array = []
for i in range(n):
    li = list(input().split())
    array.append(li)
array2=array


#장애물 3개 설치 가능한 모든 경우
obstacle = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 'X':
            obstacle.append([i,j])


obstacle = list(itertools.combinations(obstacle,3))

# print(obstacle)
#장애물 3개 가능한 모든 상황

for i in obstacle:
    stu = 0
    array2 = copy.deepcopy(array)
    for j in i:
        x,y = j
        array2[x][y] = "O"
    # print("장애물",array2)
    for a in range(n):
        for b in range(n):
            if array2[a][b] == "T":
                # print("선생님")
                #선생님이면 상하좌우 살펴보기
                for dir in range(4):
                    #학생이 발견되면, NO하고 break
                    if bfs(a,b,array2,dir):
                        stu+=1
    if stu==0:
        ans = "YES"
        break
    else:
        ans = "NO"


print(ans)

