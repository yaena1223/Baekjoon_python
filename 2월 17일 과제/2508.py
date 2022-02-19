for i in range(int(input())):
    input()
    ans = 0
    r, c = map(int, input().split())
    list1 = [[0 for col in range(c)] for row in range(r)]
    for j in range(r):
        a = input()
        for z in range(c):
            list1[j][z] = a[z]

    for x in range(r):
        for y in range(c):
            if 0 <= y < c-2 and list1[x][y] == '>' and list1[x][y + 1] == 'o' and list1[x][y + 2] == '<':
                ans = ans + 1
            if 0 <= x < r-2 and list1[x][y] == 'v' and list1[x + 1][y] == 'o' and list1[x + 2][y] == '^':
                ans = ans + 1
    print(ans)