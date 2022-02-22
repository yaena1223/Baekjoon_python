k, n = map(int,input().split())
arr = []
for i in range(k):
    arr.append(int(input()))

arr.sort()
left = 1
right = arr[-1]
while (left<=right):
    cnt = 0
    mid = (left+right)//2
    for i in range(k):
        cnt = cnt+arr[i]//mid

    if cnt < n :
        right = mid - 1
    else:
        left = mid+1

print(right)