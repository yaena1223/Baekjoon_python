'''
세준 :신상품, 최대 이익
살 의향을 보이는 사람 n명
각각 최대 한도
배달비
n명의 사람, 각각의 사람의 희망 금액, 배송비 => 세준이의 최대 이익은?

첫째줄 : n명
둘째줄 ~: 지불할 최대 금액, 배송비/

출력 : 최대이익을 만들어주는 가격
'''

n = int(input())
arr = [[col for col in range(2)]for row in range(n)]
price = []
for i in range(n):
    a, b = map(int,input().split())
    arr[i][0] = a
    arr[i][1] = b
arr.sort()
max = -1

for i in range(n):
    total_profit = 0
    price = arr[i][0]
    for j in range(n):
        profit = price - arr[j][1]
        if arr[j][0]>=price and profit > 0:
            total_profit = total_profit + profit
        if total_profit>max:
            max = total_profit
            ans = price
if max<=0:
    print(0)
else:
    print(ans)

