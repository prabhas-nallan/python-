Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup1=('phy','che',2001,2706)
>>> tup1
('phy', 'che', 2001, 2706)
>>> tup1[0]
'phy'
>>> tup1[0:4]
('phy', 'che', 2001, 2706)
>>> tup2=(465,)
>>> tup3=tup1+tup2
>>> tup3
('phy', 'che', 2001, 2706, 465)
>>> tup4=('Hello',)*5
>>> tup4
('Hello', 'Hello', 'Hello', 'Hello', 'Hello')
>>> 10 in (1,2,3,37,10)
True
>>> for x in('hlo','mam','ji',27,6,2002):
	print(x,end="\n")

	
hlo
mam
ji
27
6
2002
>>> t=45,65,2,'fell','help',3.2,-88
>>> t
(45, 65, 2, 'fell', 'help', 3.2, -88)
>>> min(t)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    min(t)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> len((56,'pull',87,2,3))
5
>>> t1=(2,5,88,97)
>>> min(t1)
2
>>> max(t1)
97
>>> 