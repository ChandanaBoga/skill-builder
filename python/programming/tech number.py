n=int(input())
count=0
while n>0:
    r=n%10
    count+=1
    n=n//10
if count%2==0:
    first=n//100
    second=n%100
    if first+second==n:
        print("tech number")
    else:
        print("not a tech number")

