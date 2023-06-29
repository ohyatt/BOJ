import sys

N,M = map(int, sys.stdin.readline().rstrip().split())

price6 = []
price1 = []

for i in range (0,M):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    price6.append(x)
    price1.append(y)

# 오름차순 정렬
price6 = sorted(price6) 
price1 = sorted(price1)

total = 0
if(price6[0] > price1[0] * 6):
    total = price1[0] * N
elif((N // 6) == 0):
    total = price1[0] * N if(price1[0]* N) < price6[0] else price6[0]
else :
    num6 = N // 6
    num1 = N % 6 
    rest = (price1[0] * num1) if (price1[0] * num1) < price6[0] else price6[0]
    total = price6[0] * num6 + rest

print(total)
