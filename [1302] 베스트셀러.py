import operator

num=int(input())

bookdict = dict()

for i in range(0,num):
    bookname = input()
    if bookname in bookdict:
        bookdict[bookname] = bookdict[bookname] + 1
    else:
        bookdict[bookname] = 1

#value값 기준으로 내림차순 정렬 
booklist = sorted(bookdict.items(),key=operator.itemgetter(1),reverse=True) 

bestseller = []
bestseller.append(booklist[0][0])

best = booklist[0][1]
for i in range(1,len(booklist)):
    if(booklist[i][1] == best):
        bestseller.append(booklist[i][0])
    else:
        break
    
bestseller = sorted(bestseller)
print(bestseller[0])
