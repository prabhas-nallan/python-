#List comprehension
lst=[2,3,4,5,6,7,8,9,10,23,25,96]
squares=[lst*lst for lst in lst if lst%2==0]
print(squares)
