n=int(input())
temp=n
n1=n**2
c=0
while n>0:
    r=n%10
    c+=1
    n=n//10
while n1>0:
    r1=n1%(10**c)
    break
if temp==r1:
    print("automorphic")
else:
    print("not automorphic")



