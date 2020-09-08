#creating lst using args
from sys import argv
import sys
a=[]
print("list a is :",a)
for i in argv[1:]:
    a.append(i)
print("List after appending:",a)

