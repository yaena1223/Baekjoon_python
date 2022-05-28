n = int(input())
p = list(map(int,input().split()))
p.sort()
sum1 = 0
for i in range(n):
    s = sum(p[:i+1])
    sum1 = sum1+s

print(sum1)