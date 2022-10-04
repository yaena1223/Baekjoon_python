#크기가 n*n인 도시
#도시는 1*1 크기의 칸으로 나누어짐
#각 칸은 빈칸/치킨집/집 중 하나
# 빈칸 : 0 , 집 : 1, 치킨집 : 2
#r행 c 열 / 1부터 시작

#치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
#도시의 치킨 거리 : 모든 집의 치킨 거리의 합
#거리 계산은 행들끼리의 차이 + 열들끼리의 차이

#가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 m개
#최대 m개를 고르고 나머지는 모두 폐업
# 어떻게 골라야 치킨거리가 가장 적을지


#출력값 : 폐업 안시킬 m개 치킨집 골랐을떄, 치킨 거리의 최솟값

#입력받기
n, m = map(int,input().split())
city = []

for i in range(n):
    inp = list(map(int,input().split()))
    city.append(inp)

# print(city)


#치킨이랑 집 좌표값 저장하고..
#치킨이랑 집 거리 계산해서, (거리, 치킨좌표) 같이 넣은 리스트 만들고 정렬하면 될거 같은..느낌쓰...

#문제 풀기

#집이랑 치킨집 좌표값 저장
chicken_list = []
house_list = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house_list.append((i,j))
        if city[i][j] == 2:
            chicken_list.append((i,j))

ans = 1e9
import itertools
# print(chicken_list)
for case in itertools.combinations(chicken_list,m):
    result = 0
    for house in house_list:
        temp = 1e9
        for chicken in case:
            # print(chicken,house)
            distance = abs(chicken[0]-house[0])+abs(chicken[1]-house[1])
            if temp > distance:
                temp = distance
        result += temp

    if result<ans:
        ans = result

print(ans)