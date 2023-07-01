import sys

N = int(sys.stdin.readline().rstrip())

time_list = list(map(int, sys.stdin.readline().rstrip().split()))
time_list.sort()

result = 0
for i in range(0,N):
    temp = time_list[i] * (N-i)
    result = result + temp

print(result)
