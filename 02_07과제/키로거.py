from collections import deque
ans_list=[]
n = int(input())
for i in range(n):
    word = input()
    front = deque()
    back = deque()
    for j in word:
        if j == '<':
            if not front:
                continue
            else:
                w = front.pop()
                back.appendleft(w)
        elif j == '>':
            if not back:
                continue
            else:
                w = back.popleft()
                front.append(w)
        elif j == '-':
            if not front:
                continue;
            else :
                front.pop()
        else:
            front.append(j)
    ans = "".join(front)+"".join(back)
    ans_list.append(ans)

for i in ans_list:
    print(i)