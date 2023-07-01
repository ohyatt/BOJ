import sys

def cal_distance(location,median,N):
    result = 0
    for i in range(0,median):
        temp = location[median] - location[i]
        result = result + temp
    for i in range(median+1,N):
        temp = location[i] - location[median]
        result = result + temp
    return result

N = int(sys.stdin.readline().rstrip())

location = list(map(int, sys.stdin.readline().rstrip().split()))
location.sort()

check_list = []
if(N % 2 == 0):
    median = N // 2
    check_list.append(cal_distance(location,(median - 1),N))
    check_list.append(cal_distance(location,median,N))
    check_list.sort()
    if(check_list[0] <= check_list[1]):
        print(location[median-1])
    else : 
        print(location[median])

else:
    median = N // 2
    print(location[median])
