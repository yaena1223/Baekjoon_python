from collections import deque

n, k = map(int,input().split())
visit = [0]*1000001
queue= deque([n])


while queue:
    x = queue.popleft()
    dx = [1,-1,x]
    for i in dx:
        x1 = x+i
        if x1>=len(visit) or x1<0:continue
        elif visit[x1]==0:
            queue.append(x1)
            if visit[x1]!=0:
                visit[x1] = min(visit[x1],visit[x]+1)
            else:
                visit[x1] = visit[x]+1
        #print(queue)
        #print(visit)
if(n==k):
    print(0)
else:
    print(visit[k])


