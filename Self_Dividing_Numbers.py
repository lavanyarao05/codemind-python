num=int(input())
r=int(input())
for i in range(num,r+1):
    first=i%10
    sec=i//10
    if i<10:
        print(i,end=" ")
    elif i>10:
        if first==0 or sec==0:
            continue
        elif i%first==0 and i%sec==0:
            print(i,end=" ")