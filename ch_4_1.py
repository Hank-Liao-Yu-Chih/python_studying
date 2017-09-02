def PrintAll (X):
	for x in X:
		print(x)
def hi ():
	print('Hi python!!')
def Listsum(L):
	result = 0
	for i in L:
		result += i
	return result
def Cube (x = None, y = None, z = 3):
	if x == None:
		x = 1
	if y == None:
		y = 2
	if z == None:
		z = 3
	return (x + y - z) ** 3	
	
print('----test the function of PrintAll')	
l = [1,2,3,4]
PrintAll(l)
t = ('a','b','c')
PrintAll(t)

print('----test the function of hi')

hi()

print('----test the function of Listsum')

l = [1,2,3,45,6,100]
r = Listsum(l)

print("r is %d\n" % r)


print('----test the function of Cube')

r = Cube()
print (r)
r = Cube(0)
print(r)
r = Cube(4,5)
print(r)
r = Cube(4,5,6)
print(r)

r = Cube(None, None, 100)
print(r)
r = Cube(None, 17, None)
print(r)	