from collections import deque
s = input()
stack = deque()
l = len(s)


#힌트 얻은 사이트 : https://pangsblog.tistory.com/53
#숫자랑 괄호가 연속으로 나오면 곱하고, 숫자랑 숫자가 나오면 더한다.
#(()[[]])([])
# 여는 괄호가 나오면, 닫는 괄호를 스택에 넣어줌
# 닫는 괄호가 나오면, 스택의 제일 끝 값과 비교하여 같으면 pop 하고, )이면 2를 ]이면 3을 스택에 넣음
tf = True
for i in range(l):
    #print(stack)
    if s[i] == "(":
        stack.append(")")
    if s[i] == "[":
        stack.append("]")
    if s[i] == ")":
        num = 0
        try:
            if stack[-1] == s[i]:
                stack.pop()
                stack.append(2)
            else:
                while type(stack[-1]) is int:
                    num = num+stack[-1]
                    stack.pop()
                if stack[-1] == s[i]:
                    stack.pop()
                    stack.append(num*2)
        except:
            tf = False
            break
    if s[i] == "]":
        num = 0
        try:
            if stack[-1] == s[i]:
                stack.pop()
                stack.append(3)
            else:
                while type(stack[-1]) is int:
                    num = num + stack[-1]
                    stack.pop()
                if stack[-1] == s[i]:
                    stack.pop()
                    stack.append(num * 3)

        except:
            tf = False
            break

#print(stack)
tf = True
for i in stack:
    if type(i) is str:
        tf = False
        break
if tf:
    ans = sum(stack)
else:
    ans = 0
print(ans)
