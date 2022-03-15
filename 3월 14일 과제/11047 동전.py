from collections import deque
n, k = map(int,input().split())
cnt = 0
l = deque()
for i in range(n):
    a = int(input())
    l.append(a)


for i in range(n-1,-1,-1):
    a = k // l[i]
    k = k % l[i]
    cnt = cnt+a
    if k==0:
        break

print(cnt)