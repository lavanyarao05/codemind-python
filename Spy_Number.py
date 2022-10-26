def spy_num(num):
    summ=0
    prod=1
    while num>0:
        d=num%10
        summ=summ+d
        prod=prod*d
        num=num//10
    if summ==prod:
        print("Spy Number")
    else:
        print("Not Spy Number")
    return
num=int(input())
spy_num(num)