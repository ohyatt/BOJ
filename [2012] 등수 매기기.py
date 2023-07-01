import sys

N = int(sys.stdin.readline().rstrip())

score_list = []
for i in range(0,N):
    score_list.append(int(sys.stdin.readline().rstrip()))

score_list.sort()

result = 0
for i in range(0,N):
    result = result + abs(score_list[i] - (i+1))

print(result)
