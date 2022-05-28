place = input()
x = int(place[1])
y = ord(place[0])-96

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

ans = 0
for i in range(8):
    new_x = x + dx[i]
    new_y = y + dy[i]
    if(new_x < 1 or new_y < 1 or new_x >8 or new_y>8):
        continue
    ans += 1

print(ans)
