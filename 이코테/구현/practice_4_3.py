
dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,-2,2,1,-1,-1,1]

i = input()
column = ord(i[0])-ord('a')+1
row = int(i[1])

ans = 0
for i in range(8):
    new_r = row + dx[i]
    new_c = column+dy[i]

    if new_c < 1 or new_c > 8 or new_r<1 or new_r>8:
        continue
    else:
        ans +=1


print(ans)