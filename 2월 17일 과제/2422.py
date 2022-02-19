n,m = map(int,input().split())
no = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    no[a].append(b)
    no[b].append(a)
cnt = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if j in no[i]:
            continue
        for z in range(j+1,n+1):
            if z in no[j] or z in no[i]:
                continue
            cnt = cnt+1

print(cnt)