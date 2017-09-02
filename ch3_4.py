dic = {'apple':2, 'orange':1}
doc = dic.copy()
print(doc)
print(dic)
dic['banana'] = 5
print('dic is:',dic)

list = dic.items()
print(list)

dic.pop('apple')
print(dic)

list = dic.keys()
print(list)

list = dic.values()
print(list)

dic.update({'banana':10})
print(dic)

print(dic['banana'])

dic.clear()

print(dic)