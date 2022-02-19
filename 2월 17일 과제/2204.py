n = -1
while n!=0:
    n = int(input())
    if n==0:
        break
    s = list()
    for i in range(n):
        word = input()
        s.append(word)
    s.sort(key = str.lower)
    print(s[0])