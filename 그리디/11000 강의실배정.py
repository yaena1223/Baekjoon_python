import heapq
import sys
n = int(input())
time_list = []
input = sys.stdin.readline
for i in range(n):
    time = list(map(int,input().split()))
    time_list.append(time)

time_list.sort(key=lambda x : (x[0],x[1]))

heap = [] #힙에 종료 시간 넣기
heapq.heappush(heap, time_list[0][1])
for i in range(1, n):
    if heap[0] <= time_list[i][0]:
        heapq.heappop(heap)
        heapq.heappush(heap,time_list[i][1])
    else:
        heapq.heappush(heap,time_list[i][1])

print(len(heap))