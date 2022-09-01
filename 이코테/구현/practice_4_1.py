import sys
input = sys.stdin.readline

n = int(input())
direction_list = list(input().split())
dx = [0,0,-1,1]
dy = [1,-1,0,0]
x = 1
y= 1
direction_title = ['R', 'L', 'U','D']
for i in direction_list:
    for j in range(4):
        if i == direction_title[j]:
            new_x = x+dx[j]
            new_y = y+dy[j]


            if new_x >n or new_y > n or new_x<=0 or new_y <=0:
                continue
            else:
                x = new_x
                y = new_y

print(x,y)