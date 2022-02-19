n = int(input())
list1 = list(map(int,input().split()))
list1.sort()
n = int(input())
list2 = list(map(int,input().split()))


def binary_search(target,num_list):
    start = 0
    end = len(num_list)-1

    while start<=end:
        mid = (start+end)//2
        if num_list[mid] == target:
            return 1
        elif num_list[mid] < target:
            start = mid+1[;]
        else:
            end = mid - 1
    return 0



for i in list2:
    print(binary_search(i,list1))
