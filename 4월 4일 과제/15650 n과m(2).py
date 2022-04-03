n, m = map(int,input().split())
arr = [0]*m
visit = [False]*(n+1)
def back(x):
    if x == m:
        print(*arr)
        return
    for i in range(1,n+1):
        if not visit[i]:
            if arr[x - 1] < i:
                arr[x] = i
                visit[i] = True
                back(x+1)
                arr[x]=0
                visit[i] = False


back(0)