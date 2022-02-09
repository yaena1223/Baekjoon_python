n, m, k = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
n1 = array[-1]
n2 = array[-2]
ans = 0
while True:
    for i in range(k):
        ans = ans+ n1
        m = m-1
    ans = ans + n2
    m = m -1
    if m==0 :
        break

print(ans)