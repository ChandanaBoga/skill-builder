n=int(input())
sum=0
mul=1
while n>0:
    r=n%10
    sum+=r
    mul*=r
    n=n//10
if sum==mul:
    print("spy number")
else:
    print("not a spy number")
