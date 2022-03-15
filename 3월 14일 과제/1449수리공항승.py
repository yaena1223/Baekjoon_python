n, l = map(int,input().split())
place = list(map(int,input().split()))
place.sort()
cnt = 1
left = place[0] - 0.5
for i in range(n-1):
    right = left + l
    if place[i+1]+0.5<=right:
        continue
    else:
        cnt = cnt+1
        left = place[i+1] - 0.5

print(cnt)