word = input()
ans_list = set()
l = len(word)
for i in range(l):
    for j in range(i+1,l+1):
        word2 = word[i:j]
        ans_list.add(word2)

print(len(ans_list))