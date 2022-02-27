'''

각각의 보석은 서로 다른 색상 중 한 색상
모든 보석을 na여의 학생에게 나눔
(보석을 받지 못하는 학생 있어도 됨)
(학생은 같은 색상만)
질투심 : 가장 많은 보석을 가져간 학생이 가지고 있는 보석의 개수
질투심이 최소가 되게 나누어주는 방법은?
'''
import heapq
import sys
input = sys.stdin.readline
n, m = map(int,input().split())

color = []
for i in range(m):
    heapq.heappush(color,-int(input()))

#print(color)
num = len(color)
while(num<n):
    q = color[0]
    a = q//2
    b = q - a
    heapq.heappop(color)
    heapq.heappush(color,a)
    heapq.heappush(color,b)
    num = len(color)

print(-color[0])