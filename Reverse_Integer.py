n=int(input())
s=str(n)
l=len(s)
b=n
k=0
if n<0:
    n=abs(n)
    for i in range(l-1):
        k=k*10+(n%10)
        n=n//10
    k=abs(k)
    print(-k)
elif n>0:
    for j in range(l):
        k=k*10+(n%10)
        n=n//10
    print(k)