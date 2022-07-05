n = int(input())
time_list = []
for i in range(n):
    time = list(map(int,input().split()))
    time_list.append(time)

time_list.sort(key=lambda x:(x[1],x[0]))
cnt = 1
end = time_list[0][1]
i = 1
while(i<n):
    if time_list[i][0]>=end:
        cnt +=1
        end = time_list[i][1]
    i+=1

print(cnt)