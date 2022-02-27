'''
n개의 줄이 끊어짐
6줄 패키지 or 1개 또는 그 이상을 낱개로 삼

'''
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
min_one = 1000
min_six = 1000
for i in range(m):
    a,b = map(int,input().split())
    if a<min_six:
        min_six = a
    if b<min_one:
        min_one= b
x=0
if n%6==0:
    x = n//6
else:
    x = n//6+1
ans = 100000

for i in range(x+1):
    y = n-i*6
    if i == x:
        y = 0
    price = min_six * i + min_one * y
    if price<ans:
        ans = price

print(ans)