def solution(key, lock):
    #(m,m에 있는 값이 0,0이 되는 것부터 0,0에 있는 값이 n,n이 되는 곳까지 완전탐색)
    #lock 배열을 새롭게 만듦
    m = len(key)
    n = len(lock)

    new_lock = [[0 for i in range(n+2*m-2)] for j in range(n+2*m-2)]
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 1:
                new_lock[i+m-1][j+m-1] = 1

    # for i in new_lock:
    #     print(i)

    # 회전 90, 180, 270, 360(0)
    for i in range(4):
        key = turn(key)
        # print("key",key)

        #제일 왼쪽 위부터, (0~m)을 더한 좌표값이 제일 오른쪽 아래 값이 되는 범위까지 (n+2*m-1,n+2*m-1)
        for j in range(0, n+m-1):
            for z in range(0,  n+m-1):
                for x in range(m):
                    for y in range(m):
                        new_lock[j+x][z+y] += key[x][y]

                if check(m,n,new_lock):
                    # print(new_lock)
                    return True

                else:
                    for x in range(m):
                        for y in range(m):
                            new_lock[j+x][z+y] -= key[x][y]



    return False


#(m-1,m-1)부터 (n+m-2,n+m-2)까지의 범위에 1이 아닌 값이 있으면 False(전체 다 1이여야함)
def check(m,n,lis):
    ans = 0
    for i in range(m-1,n+m-1):
        for j in range(m-1,n+m-1):
            # print(i,j)
            if lis[i][j]!=1:
                return False

    return True

#회전
def turn(key):
    n = len(key)
    new_list = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            x, y = j, n-i-1
            if key[i][j] == 1:
                new_list[x][y] = 1


    return new_list



print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))