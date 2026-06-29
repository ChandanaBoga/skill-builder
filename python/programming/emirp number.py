def is_prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
    return False
n=int(input())
c=0
if is_prime(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if is_prime(rev):
        c+=1
        print("emirp number")
if c==0:
    print("not emirp number")


