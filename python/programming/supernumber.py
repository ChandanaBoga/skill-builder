n=int(input())
temp=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
c=0
sum=0
while rev>0:
    r=rev%10
    c+=1
    sum=sum+(r**c)
    rev=rev//10
if temp==sum:
    print("super number")
else:
    print("not super number")