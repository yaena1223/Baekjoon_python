'''
학생 n명의 이름
국, 영, 수 점수
- 국어 점수 감소하는 순서
- 국어 같으면, 영어 점수 증가하는 순서
- 국, 영 같으면 수학 감소하는 순서
- 모두 같으면, 이름 사전 순 (대문자는 소문자보다 작으므로 사전순으로 앞에 옴)


'''
import sys
n = int(input())
student = []
for i in range(n):
    input = list(sys.stdin.readline().split()) # 이름,국, 영, 수 입력 받고 리스트에 저장
    student.append(input)

student.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in student:
    print(i[0])