#Dictionary comprehension
d={}
print(type(d))
n=int(input())#key value pairs
for i in range(n):
    print("enter key",end='')
    x=int(input())
    print("enter value",end='')
    y=x*x
    d.update({x:y})
    print("Dict is:",d)
