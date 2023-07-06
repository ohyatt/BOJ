import sys
from itertools import combinations

# 스타트팀과 링크팀 각각의 합을 구하는 함수 
def cal_sum(player,startlink): # player : 선수 간의 능력치를 나타낸 2차원 리스트 / startlink : 스타트팀 또는 링크팀에 속한 선수를 나타낸 리스트
    sum = 0
    for i in startlink:
        for j in startlink:
            if(j > i):
                sum = sum + player[i-1][j-1] + player[j-1][i-1]
    return sum 

N = int(sys.stdin.readline().rstrip())

# 선수의 수만큼 번호가 차례대로 매겨진 리스트 생성
numOfplayer = []
for i in range(0,N):
    numOfplayer.append(i+1)

# 선수 간의 능력치를 나타 낸 2차원 배열 입력
player = []
for i in range(0,N):
    player.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = 100
# 선수들을 반으로 나눠 팀을 형성할 수 있는 조합 리스트
team = list(combinations(numOfplayer, N // 2))
for i in range(0, len(team) // 2):
    start = team[i]
    sTemp = cal_sum(player,start)
    link = team[-1-i]
    lTemp = cal_sum(player,link)
    
    # 두 팀 간 능력치 합의 차는 음수가 될 수 있으므로 절댓값으로 처리
    if (abs(sTemp - lTemp) < result):
        result = abs(sTemp - lTemp)

print(result)

