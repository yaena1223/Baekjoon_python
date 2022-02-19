import sys
m = int(input())
s = set()
for i in range(m):
    a= sys.stdin.readline().split()
    input1 = a[0]
    if len(a) == 2:
        input2 = int(a[1])
    if input1 == "add":
        s.add(input2)
    if input1 == "check":
        if input2 in s:
            print(1)
        else:
            print(0)
    if input1 == "remove":
        if len(s)==0:
            continue
        else:
            s.remove(input2)
    if input1 == "toggle":
        if input2 in s:
            s.remove(input2)
        else:
            s.add(input2)
    if input1 == "empty":
        s.clear()
    if input1 == "all":
        s = {i for i in range(1,21)}

