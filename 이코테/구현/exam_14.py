#구조 동그란 모양, 외벽 총 둘레는 n미터, 추위가 심하면 손상될 수 있는 취약지점 존재
# => 친구들이랑 주기 점검 , 점검 시간 1시간 제한
# 친구들 : 1시간 동안 이동할 수 있는 거리는 제각각 
# 최소한의 친구가 점검, 나머지 친구는 내부 공사
# 정북 방향 지점 : 0, 취약지점의 위치는 시계방향으로 떨어진 거리로 나타냄
# 출발지점, 시계/반시계 방향으로 외벽만 따라서 이동
#n : 외벽 길이, weak : 취약 지점 위치, dist : 친구들이 1시간 동안 이동 가능한 거리
# (weak) 취약지점 위치 길이는 1-15까지, 오름차순 정렬
# dist는 1이상 8이하(친구 8명 이하)
#출력값 : 친구 모두 투입해도, 취약지점 점검 불가면 -1, 아니면 취약지점 점검 최소인원 출력
from itertools import permutations


#문제 풀이 방법
#원형을 일자로 변경 => 길이 * 2
#친구 경우의 수 전체 (순열)
#완전탐색 => 친구 인원 count. 가능한 경우 없으면 -1

def solution(n, weak, dist):
    length = len(weak)
    
    #원형을 일자로 변경
    for i in range(length):
        weak.append(weak[i]+n)
    # print(weak)
    #최소값 구하는 문제이므로 젤 큰 경우 + 1을 초기값으로 잡아줌
    answer = len(dist)+1
    
    #가능한 모든 경우의 수 완전 탐색(시작점)
    for start in range(length):
        #친구 순서 모든 순열
        for friends in list(permutations(dist,len(dist))):
            count = 1
            #마지막 지점
            position = weak[start] +friends[count-1]
            # print(position)
            #시작점부터 끝까지 
            for index in range(start, start+length):
                #탐색 가능한 마지막 점보다 취약점 좌표가 크면, 인원 추가 
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(count, answer)
        
    if answer > len(dist):
        return -1
                    
    return answer
