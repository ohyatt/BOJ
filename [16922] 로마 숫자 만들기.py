import sys
from itertools import * 

N = int(sys.stdin.readline().rstrip())

roma_list = [1,5,10,50]
num_list = list(combinations_with_replacement(roma_list,N))
result = []

for i in num_list:
    result.append(sum(i))

result = set(result)
print(len(result))
