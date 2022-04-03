pibo_list = [0 for i in range(68)]
pibo_list[0] = 1
pibo_list[1] = 1
pibo_list[2] = 2
pibo_list[3] = 4
for i in range(4,68):
    pibo_list[i] = pibo_list[i-1]+pibo_list[i-2]+pibo_list[i-3]+pibo_list[i-4]
t = int(input())
for i in range(t):
    n = int(input())
    print(pibo_list[n])
