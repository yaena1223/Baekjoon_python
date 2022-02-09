a = int(input())
stack_array = []
ans = []
num = 1
tf = True
for i in range(a):
    x = int(input())
    while x >= num:
        stack_array.append(num)
        ans.append('+')
        num += 1
    if stack_array[-1] == x:
        stack_array.pop()
        ans.append('-')
    else:
        tf = False


if tf:
    print("\n".join(ans))

else:
    print("NO")
