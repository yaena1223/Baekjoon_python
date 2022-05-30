import heapq
from collections import defaultdict
import sys
t = int(input())
for i in range(t):
    k = int(input())
    min_queue = []
    max_queue = []
    dict = defaultdict(int) #default 딕셔너리는 기본으로 0값이 들어 있음
    input = sys.stdin.readline
    for j in range(k):
        id, num = input().split()

        if id == "I":
            heapq.heappush(min_queue,int(num))
            heapq.heappush(max_queue, -1*int(num))
            dict[int(num)] += 1


        if id == "D":
            if num == '-1': #최소값 삭제
                while(True):
                    if len(min_queue) == 0:
                        break
                    else:
                        delete_num = min_queue[0]
                        if dict[delete_num] != 0:
                            dict[delete_num] -= 1
                            heapq.heappop(min_queue)
                            break
                        if dict[delete_num] == 0:
                            heapq.heappop(min_queue)


            if num == '1': #최대값 삭제

                while(True):
                    if len(max_queue)==0:
                        break
                    else:
                        delete_num = -1*max_queue[0]
                        if dict[delete_num]!= 0:
                            dict[delete_num] -= 1
                            heapq.heappop(max_queue)
                            break
                        if dict[delete_num] == 0:
                            heapq.heappop(max_queue)

    cnt = 0
    num = 0
    ans = ""
    tmp = dict.keys()
    # print(dict)
    max_v = -999999999
    min_v = 999999999
    for i in tmp:
        if dict[i]:
            cnt +=1
            if i > max_v: max_v = i
            if i < min_v: min_v = i
            num = i
    if cnt == 0:
        print("EMPTY")
    elif cnt == 1:
        print(num,num)
    else:
        print(max_v, min_v)
        # print(-1*max_queue[0],min_queue[0])



