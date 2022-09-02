s = input()
word = []
number = []

for i in s:
    if ord(i) >= ord('A'):
        word.append(i)
    else:
        number.append(int(i))

word.sort()

print("".join(word),end="")
print(sum(number))