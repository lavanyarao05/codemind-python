n=int(input())
a=0
b=1
c=0
l1=[]
l2=[]
for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    if c<n:
        l1.append(b)
    else:
        l2.append(b)
x=n-max(l1)
y=min(l2)-n
if x<y:
    print(max(l1))
elif x>y:
    print(min(l2))
elif x==y:
    print(max(l1),min(l2))