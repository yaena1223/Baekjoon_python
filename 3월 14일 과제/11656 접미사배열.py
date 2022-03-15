s = input()
l = []
for i in range(len(s)):
    word = s[i:]
    l.append(word)

l.sort()
for i in l:
    print(i)