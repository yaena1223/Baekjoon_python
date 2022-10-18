def solution(p):
    answer = ''
    if p == '':
        return answer
    
    bal = balance(p)
    # print(bal)
    u = p[:bal+1]
    v = p[bal+1:]
    print(u,v)
    # print(u,v)
    print(bal)
    if check(u):
        answer = u + solution(v)
        # print(answer)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = u[1:-1]
        for i in u:
            if i == "(":
                answer += ")"
            else:
                answer += "("

            
            
    return answer

#균형잡힌 괄호 문자열
def balance(p):
    count = 0 
    for i in range(len(p)):
        if p[i] == "(":
            count+=1
        else:
            count-=1
        if count==0:
            return i

#올바른 문자열인지 판별하는 함수
def check(p):
    #괄호 확인
    #여는 괄호 나오면 스택에 넣고, 닫는 괄호 나오면 스택에서 pop을 함
    #마지막에 스택 비어 있으면 true, 아니면 false반환
    stack = []
    for i in p:
        if i == "(":
            stack.append("(")
        if i == ")" and stack:
            stack.pop()
    if len(stack) !=0:
        return False
    return True
