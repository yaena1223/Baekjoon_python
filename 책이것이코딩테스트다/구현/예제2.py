n = int(input())
ans = 0
for i in range(n+1):
    for j in range(60):
        for z in range(60):
            if '3' in str(i) or '3' in str(j) or '3' in str(z):
                ans +=1

print(ans)