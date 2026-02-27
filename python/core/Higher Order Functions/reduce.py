from functools import reduce

lists=[1,2,3,4,5,6,7,8,9,10]
result=reduce(lambda a,b : a if  a>b else b , lists)
print(result)



