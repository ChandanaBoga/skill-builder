n=int(input())
n1=int(input())
a=0
b=1
for i in range(1,n+1):
    print(a,end=" ")
    if a==n1:
        break
    sum = a + b
    a = b
    b = sum
if a==n1:
    print("fibonacci number")
else:
    print("not a fibonacci number")