n, m = map(int,input().split())
list_idpw = {}
for i in range(n):
    site, pw = input().split()
    list_idpw[site] = pw
#print(list_idpw)
for i in range(m):
    find_site = input()
    print(list_idpw[find_site])

