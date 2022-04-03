
word = list(input())
w = ['P','P','A','P']
stack = []
for i in word:
    stack.append(i)
    if stack[-4:]==w:
        stack.pop()
        stack.pop()
        stack.pop()
#print(stack)
if stack ==['P']:
    print("PPAP")
else:
    print("NP")
