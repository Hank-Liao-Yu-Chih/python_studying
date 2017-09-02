import math

a=1
b=2

if (a == b):
	print('true')
else:
	print('false')

if (a < b):
	print('true')
else:
	print('false')

m = 'hi'
n = 'hello'

if (m == n):
	print('true')
elif (m > n):
	print('false')
else:
	print(m,n)

l1 = [1,2]	
l2 = [3,4]

if (l1 == l2):
	print('true')

if (l1 != l2):
	print('false')

if (l1 <= l2):
	print('true')

if not 1:
	print('true')
else:
	print('false')


print('---------for loop test-------')


for i in [1,2,3,4,5,6]:
	if (i == 6):
		break;
	if (i == 2):
		continue
	print(i)
print('all')

for i in range(1,6):
	print(i)

for i in range(0,11,2):
	print(i)


people = {'Tom':170, 'Jack':180, 'Kite':160, 'White':180}

for name in people:
	print(people[name],name)


tt = (('a','b'), ('c', 'd'), ('e','f'),('g','h'))
for t1 in tt:
	print(t1)
for (x,y) in tt:
	print(x,y)


#----find prime number

print("find the prime number from 50 ~ 100")

for i in range(50, 101):
	for t in range(2, int(math.sqrt(i)) + 1):
		if (i % t) == 0:
			break;
	else:		
		print(i)

#-------while loop test-------

print("while loop test")
x=1
while (x <= 5):
	print(x)
	x=x + 1	