n, m = map(int,input().split())
visit = [False]*(n+1)
arr = [0]*m

def back(x):
    if(x==m):
        print(*arr)
        return
    for i in range(1,n+1):
        if not visit[i]:
            arr[x] = i
            visit[i] = True
            back(x+1)
            arr[x] = 0
            visit[i] = False
back(0)