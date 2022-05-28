n = int(input())
plan = list(input().split())
x = 1
y = 1

move= ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for i in plan:
    for j in range(4):
        if i == move[j]:
            new_x = x + dx[j]
            new_y = y + dy[j]
    if new_x < 1 or new_y <1 or new_x >n or new_y >n:
        continue
    x = new_x
    y = new_y

print(x,y)