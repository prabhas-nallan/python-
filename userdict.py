#create dict from keyboard
a={} #taking empty dict
print(type(a))
print("how many elements?",end='')
n=int(input()) #indicates no of key value pairs
for i in range(n):
    print("Enter key:",end='')
    x=input()#key is string
    print("Enter values:",end='')
    y=input()#value is integer
    a.update({x:y})
    #display dict
    print("dictionary is:",a)
