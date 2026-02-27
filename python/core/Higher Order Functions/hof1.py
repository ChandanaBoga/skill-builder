# 1
# l=[[1,2],[3,4],[5,6]]
# x=list(map(lambda x:x+[5],l))
# print(x)

# 2
# d={"apple":100, "banana":40, "cherry":150}
# print(d.keys())
# print(d.values())
# print(d.items())
# f= dict(filter(lambda x:x[1]>50,d.items()))
# print(f)

#3
# k=input()
# print(k.split())
# print(type(k))

# k=list(map(int,input().split()))
# m=-10**6
# for i in k:
#     if m<i:
#         m=i
# from functools import reduce
# print(reduce(lambda x,y:x if x>y else y, k))


# 10
# from functools import reduce
# l=[5,10,15,20,25,30]
# sq=list(map(lambda x:x**2,l))
# print(sq)
# di=list(filter(lambda x:x%5==0,sq))
# v= reduce(lambda x,y:x+y,di)
# print(v)
#
# c=reduce(lambda x,y:x+y,filter(lambda x:x%5==0,map(lambda x:x**2,l)))
# print(c)








