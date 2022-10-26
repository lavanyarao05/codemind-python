n=int(input())
for x in range(1,n+1):
    s=x*(x+1)
    if n!=s:
        res=0
    else:
        res=1
        break
if res==1:
    print("YES")
if res==0:
    print("NO")