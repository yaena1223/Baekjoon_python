# + - x / 순
#pypy로 하면 정답, python으로 하면 시간초과 뜸 ㅜ
#백준 14888 연산자 끼워넣기

n = int(input())
num_list = list(map(int,input().split()))
cal_list = list(map(int,input().split()))
cal = []
c = ["+","-","*","/"]
for i in range(4):
    if cal_list[i]!=0:
        for j in range(cal_list[i]):
            cal.append(c[i])


from itertools import permutations
cal = list(permutations(cal,len(cal)))
min_num = 1e9
max_num = -1e9

for i in cal:
    ans = num_list[0]
    for j in range(n-1):
        if i[j] == "+":
            ans += num_list[j+1]
        if i[j] == "-":
            ans -= num_list[j + 1]
        if i[j] == "*":
            ans *= num_list[j + 1]
        if i[j] == "/":
            if ans>0:
                ans //= num_list[j + 1]
            else:
                ans = -(-ans//num_list[j + 1])

    min_num = min(ans,min_num)
    max_num = max(ans,max_num)


print(max_num)
print(min_num)