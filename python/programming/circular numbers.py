n=int(input())
temp=n
c=0
while temp>0:
    r=temp%10
    c+=1
    temp=temp//10
i=1
while i<=c:
    r=n%10
    n=n//10
    res=(10**(c-1))*r+n
    print(res)
    n=res
    i+=1
