Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dictionary
>>> d1={"sno":525,"sname":"prabhas","year":2001}
>>> print(type(d1))
<class 'dict'>
>>> d1
{'sno': 525, 'sname': 'prabhas', 'year': 2001}
>>> print(d1['sno'])
525
>>> print(d1['sname'])
prabhas
>>> #change values
>>> d1['sno']=527
>>> d1
{'sno': 527, 'sname': 'prabhas', 'year': 2001}
>>> #loop in dict
>>> for i in d1.keys:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    for i in d1.keys:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for i in d1:
	print(i)

	
sno
sname
year
>>> for i in d1:
	print(d1[i])

	
527
prabhas
2001
>>> for i in d1.items():
	print(i)

	
('sno', 527)
('sname', 'prabhas')
('year', 2001)
>>> #length
>>> print(len(d1))
3
>>> #adding items
>>> d1
{'sno': 527, 'sname': 'prabhas', 'year': 2001}
>>> d1["mobno"]=9390
>>> d1
{'sno': 527, 'sname': 'prabhas', 'year': 2001, 'mobno': 9390}
>>> #pop
>>> d1
{'sno': 527, 'sname': 'prabhas', 'year': 2001, 'mobno': 9390}
>>> d1.pop("sno")
527
>>> d1
{'sname': 'prabhas', 'year': 2001, 'mobno': 9390}
>>> #delete
>>> d1
{'sname': 'prabhas', 'year': 2001, 'mobno': 9390}
>>> del d1["year"]
>>> d1
{'sname': 'prabhas', 'mobno': 9390}
>>> del d1
>>> d1
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d1
NameError: name 'd1' is not defined
>>> #clear
>>> d={"name":"ram","college":"cvr","id":19525}
>>> d
{'name': 'ram', 'college': 'cvr', 'id': 19525}
>>> d.clear()
>>> d
{}
>>> #copy dict
>>>  d={"name":"ram","college":"cvr","id":19525}
 
SyntaxError: unexpected indent
>>> d={"name":"ram","college":"cvr","id":19525}
>>> d1=d.copy()
>>> d1
{'name': 'ram', 'college': 'cvr', 'id': 19525}
>>> d2=dict(d1)
>>> d2
{'name': 'ram', 'college': 'cvr', 'id': 19525}
>>> #nested dicts
>>> college={"st1":{"name":"raj","year":2020},"st2":{"name":"kumar","year":2019}}
>>> college
{'st1': {'name': 'raj', 'year': 2020}, 'st2': {'name': 'kumar', 'year': 2019}}
>>> #dict constructor
>>> di=dict(brand="rolex",model="fastrack",year=1947)
>>> print(type(di))
<class 'dict'>
>>> di
{'brand': 'rolex', 'model': 'fastrack', 'year': 1947}
>>> #checking key existence
>>> di
{'brand': 'rolex', 'model': 'fastrack', 'year': 1947}
>>> if 'model' in di:
	print("yes")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if 'model' in di:
	print("yes")

	
yes
>>> if 'model' in di:
	print("yes")
else:
	print("not available")

	
yes
>>> di.update({"mobile":762446})
>>> di
{'brand': 'rolex', 'model': 'fastrack', 'year': 1947, 'mobile': 762446}
>>> 
>>> 
>>> #create dict from keyboard
>>> 
=========================================================================== RESTART: F:/python prgms/userdict.py ===========================================================================
Traceback (most recent call last):
  File "F:/python prgms/userdict.py", line 3, in <module>
    print(type(x))
NameError: name 'x' is not defined
>>> 
=========================================================================== RESTART: F:/python prgms/userdict.py ===========================================================================
<class 'dict'>
how many elements?3
Enter key:name
Enter values:45
dictionary is: {'name': 45}
Enter key:phnno
Enter values:9949013040
dictionary is: {'name': 45, 'phnno': 9949013040}
Enter key:rollno
Enter values:525
dictionary is: {'name': 45, 'phnno': 9949013040, 'rollno': 525}
>>> college
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    college
NameError: name 'college' is not defined
>>> college={"st1":{"name":"raj","year":2020},"st2":{"name":"kumar","year":2019}}
>>> college
{'st1': {'name': 'raj', 'year': 2020}, 'st2': {'name': 'kumar', 'year': 2019}}
>>> #nested calls
>>> print(college["st2"]["name"])
kumar
>>> 
=========================================================================== RESTART: F:/python prgms/userdict.py ===========================================================================
<class 'dict'>
how many elements?2
Enter key:name
Enter values:prabhaas
dictionary is: {'name': 'prabhaas'}
Enter key:address
Enter values:vasantham
dictionary is: {'name': 'prabhaas', 'address': 'vasantham'}
>>> 