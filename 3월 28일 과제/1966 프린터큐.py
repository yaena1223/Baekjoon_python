from collections import deque
num = int(input())
for i in range(num):
    n, m = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    cnt = 0
    while queue:
        max_num = max(queue)
        first = queue.popleft()
        m = m-1

        if max_num == first:
            cnt +=1
            if m<0:
                print(cnt)
                break
        else:
            queue.append(first)
            if m<0:
                m = len(queue)-1



'''

max 값 저장
'''