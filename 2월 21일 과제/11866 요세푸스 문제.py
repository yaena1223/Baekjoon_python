from collections import deque
n, k = map(int,input().split())
arr = [i+1 for i in range(n)]
queue = deque(range(1,n+1))
print("<", end="")
ans = ""
while(True):
    if len(queue)==0:
        break
    for i in range(k):
        p = queue.popleft()
        if i==k-1:
            ans = ans+str(p)+", "
        else:
            queue.append(p)

print(ans[:-2],end="")
print(">")