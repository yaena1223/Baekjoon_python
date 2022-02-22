'''상근이 숫자 카드 n개 가지고 있음
둘째줄 상근이 가진 카드
셋째줄 비교할 숫자 m개
넷째줄 m개의 숫자
출력 : 있는지 없는지 (1,0)
'''
n = int(input())
arr1 = set(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
for i in arr2:
    if i in arr1:
        print(1,end=" ")
    else:
        print(0,end=" ")
