#n*n 시험관
#특정 위치에 바이러스 존재 가능/ 바이러스 종류는 1~K번까지 K가지
# 모든 바이러스는 1초마다 상하좌우 방향으로 증식. 번호 낮은 종류의 바이러스부터 증식
#이미 바이러스 있으면, 다른 바이러스 못들어감
#출력값 : s초가 지난 후 (x,y)에 존재하는 바이러스의 종류 / 없으면 0 출력
#1,1부터임 (0,0 아님)

from collections import deque
import heapq
n, k = map(int,input().split())
test = []
heap = []
for i in range(n):
    a = list(map(int,input().split()))
    test.append(a)
    for j in range(n):
        if a[j] !=0:
            heapq.heappush(heap,(a[j],i,j))


s,input_x,input_y = map(int,input().split())

# print(heap)
dx = [0,0,1,-1]
dy = [1,-1,0,0]
time = 0
# print(test)
while True:
    time+=1
    if time == s+1:
        break
    # print()
    # print("time", time)
    temp = []
    while heap:

        # print("heap",heap)
        a,x,y = heapq.heappop(heap)
        # print(a,x,y)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # print("new_x:",new_x,"new_y:",new_y)
            if new_x <0 or new_y <0 or new_x >=n or new_y>=n:
                continue
            elif test[new_x][new_y] == 0 :
                test[new_x][new_y] = a
                heapq.heappush(temp,(a,new_x,new_y))
                # print("채우기, test", test)

            else:
                continue

    for z in temp:
        a,b,c = z
        heapq.heappush(heap,(a,b,c))
# print(time)
print(test[input_x-1][input_y-1])