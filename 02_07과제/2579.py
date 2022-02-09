from collections import deque
n = int(input())
num_list = deque()
max_list = deque()
for i in range(n):
    num = int(input())
    num_list.append(num)
if(n==1):
    print(num_list[0])
if(n==2):
    print(num_list[0]+num_list[1])
if(n>=3):
    max_list.append(num_list[0])
    max_list.append(max(num_list[0]+num_list[1],num_list[1]))
    max_list.append(max(num_list[0]+num_list[2],num_list[1]+num_list[2]))
    for i in range(3,n):
        max_list.append(max(max_list[i-2]+num_list[i],max_list[i-3]+num_list[i-1]+num_list[i]))

    print(max_list.pop())