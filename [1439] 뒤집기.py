num = input()

tmp = num[0]
cnt1 = 0
cnt2 = 0

for i in range(1,len(num)):
    if(num[i] == tmp):
        continue
    else :
        if(num[i-1] == num[0]):
            cnt1 = cnt1 + 1
        else :
            cnt2 = cnt2 + 1
        tmp = num[i]
        
if(tmp == num[0]):
    cnt1 = cnt1 + 1
else:
    cnt2 = cnt2 + 1
        
if(cnt1 > cnt2):
    print(cnt2)
else:
    print(cnt1)
