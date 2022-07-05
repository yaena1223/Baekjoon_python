s = input()
#오른쪽에 있는 값이 왼쪽에 있는 값보다 크면 곱하는게 숫자가 큼.
ans = int(s[0])
for i in range(len(s)-1):
    if int(s[i]) <=1 or int(s[i+1])<=1:
        ans += int(s[i+1])
    else:
        ans *=int(s[i+1])

print(ans)