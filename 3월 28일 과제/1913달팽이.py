n = int(input())
m = int(input())
lis = [[0 for i in range(n)]for j in range(n)]

num = n*n
dx = [1,0,-1,0]
dy = [0,1,0,-1]
x = 0
y = 0
i = 0
lis[0][0] = n*n
while(True):
    new_x = x+dx[i]
    new_y = y+dy[i]
    if new_x>=n or new_y>=n or new_x<0 or new_y<0 or lis[new_x][new_y]!=0:
        i = (i+1)%4
    x = x+dx[i]
    y = y+dy[i]
   #print(x, y)
    num = num-1
    lis[x][y] = num
    if num==1:
        break
for i in range(n):
    print(*lis[i])
for i in range(n):
    for j in range(n):
        if lis[i][j] == m:
            print(i+1,j+1)