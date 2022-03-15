word = input()
find = input()
l = len(find)
ans = 0
for i in range(l):
    cnt = 0
    while(i+l<=len(word)):
        if word[i:i+l]==find:
            i = i+l
            cnt += 1
        else:
            i +=1
    ans = max(ans,cnt)

print(ans)
