
def cal(word_list):
    cnt = 1
    ans = ""
    for i in range(1,len(word_list)):
        if word_list[i-1]==word_list[i]:
            cnt +=1
        else:
            if cnt == 1:
                ans = ans + word_list[i-1]
            else:
                ans = ans + str(cnt)+word_list[i-1]
            cnt = 1
    if cnt == 1:
        ans = ans + word_list[i]
    else:
        ans = ans + str(cnt) + word_list[i]
    cnt = 1
    return ans

def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        temp_list = []
        for j in range(len(s)//i):
            temp_list.append(s[j*i:j*i+i])
        if s[len(s) // i * i:]!="":
            temp_list.append(s[len(s) // i * i:])
        ans_word = cal(temp_list)
        if len(ans_word)<answer:
            answer = len(ans_word)
    return answer

print(solution("aaaaaaaaabaa"))