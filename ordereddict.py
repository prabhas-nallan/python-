import collections
print('Ordered dictionary:')
d=collections.OrderedDict()
d['a']='A'
d['b']='B'
d['c']='C'
d['d']='D'
d['e']='E'
for k,v in d.items():
    print(k,v)
