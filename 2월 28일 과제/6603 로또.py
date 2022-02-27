'''
6개를 고름
49가지 수 중 k개의 수를 골라 집합 s를 만들고, 그 수만 가지고 번호를 선택

'''
import sys

input = sys.stdin.readline



def back(l, x, k):
    if x == 6:
        for i in range(6):
            print(arr[i], end=" ")
        print()
        return

    for i in range(k):
        if not visited[i] and arr[x-1]<l[i]:
            arr[x] = l[i]
            visited[i]=True
            back(l,x+1,k)
            visited[i] = False
            arr[x]=0

k = -1
while k != 0:
    inp = list(map(int, input().split()))
    k = inp[0]
    list1 = inp[1:]
    arr = [0] * 6
    visited = [False] * k
    back(list1,0,k)
    print()