S = input()

sublist = []
for i in range(0,len(S)):
    for k in range(i+1,len(S)+1):
        s = S[i:k]
        sublist.append(s)

sublist = set(sublist)
result = len(sublist)

print(result)
