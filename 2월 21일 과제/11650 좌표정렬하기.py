n = int(input())
list_num = [[0 for col in range(2)]for row in range(n)]
for i in range(n):
    x, y = map(int,input().split())
    list_num[i][0] = x
    list_num[i][1] = y

list_num.sort()

for i in range(n):
    print(list_num[i][0],end=" ")
    print(list_num[i][1])