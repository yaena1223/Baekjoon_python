n, m = map(int,input().split())
l = list(map(int,input().split()))

end = 0
cnt = 0
s = 0
for start in range(n):
    #print(start,"start")
    while(s<m and end<n):
        s += l[end]
        end +=1

    if s==m:
        cnt+=1
    s -= l[start]
    #print(s)
print(cnt)