#한 번에 한 명의 유저 신고
#신고 횟수 제한 X , 다른 유저 계속 신고 가능
# 한 유저를 여러번 신고 가능하지만, 동일한 유저에 대한 신고 횟수는 1회로 처리 됨

#k번 이상 신고된 유저는 이용 정지, 정지된 사실을 신고한 유저들에게 알림
#마지막에 한꺼번에 이용 정지 시키면서 정지 메일 발송

def solution(id_list, report, k):

    #신고 리스트
    send_report = dict()
    for i in id_list:
        send_report[i] = []

    # print(send_report)

    #신고 받은 횟수 딕셔너리
    receive_report = dict()
    for i in id_list:
        receive_report[i] = 0

    for i in report:
        send, receive = i.split()
        if receive not in send_report[send]:
            receive_report[receive] += 1
            send_report[send].append(receive)
    # print(receive_report)
    # print(send_report)
    answer = []
    for key in send_report:
        ans = 0
        for i in send_report[key]:
            if receive_report[i]>=k:
                ans += 1
        answer.append(ans)


    return answer

print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))
print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))