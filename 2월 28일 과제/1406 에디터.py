import sys

word = input()
m = int(input())
from collections import deque
stack = deque(word)
queue = deque()
for i in range(m):
    order = list(sys.stdin.readline().split())
    o = order[0]
    if o == "P":
        stack.append(order[1])
    elif o == "L":
        if len(stack)>0:
            a = stack.pop()
            queue.appendleft(a)
    elif o == "D":
        if len(queue)>0:
            a = queue.popleft()
            stack.append(a)
    elif o == "B":
        if len(stack)>0:
            stack.pop()


answer = stack + queue
print(''.join(answer))