n = int(input())
dae = {} # 딕셔너리로 저장
yeong = []
for i in range(n):
    car_num = input()
    dae[car_num] = i #딕셔너리의 key값을 차번호로, i값을 순서로 저장
for i in range(n):
    car_num = input()
    yeong.append(car_num) #그냥 차번호 저장

num_list = []
for i in yeong: #딕셔너리의 key값과 yeong의 차번호를 비교하여, 일치하면 딕셔너리의 value값(원래 순서) 을 저장
    if i in dae:
        num_list.append(dae[i])
#print(num_list)
ans = 0
for i in range(n): #앞에 있는 숫자가 뒤에 있는 숫자보다 크면, 추월한거이므로 +1
    for j in range(i,n):
        if num_list[i] > num_list[j]:
            ans = ans+1
            break

print(ans)