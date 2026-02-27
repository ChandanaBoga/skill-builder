n=int(input())
fc=0
temp=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
for i in range(1,rev+1):
    if rev%i==0:
        fc+=1
if fc==2:
    print("emirp number")
else:
    print("not an emirp number")
