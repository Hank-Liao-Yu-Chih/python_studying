class A:
	name = 'A'
	__num = 1
	def show(self):
		print(self.name)
		print(self.__num)
	def setnum(self,num):
		self.__num

class B:
	nameb = 'B'
	__numb = 2
	def show(self):
		print(self.nameb)
		print(self.__numb)
	def setname(self,name):
		self.nameb = name

class C(A,B):
	def showall(self):
		print(self.name)
		print(self.nameb)
	show = B.show	
		
class human:
	__age = 0
	__sex = ''
	__height = 0
	__weight = 0
	name = ''
	def __init__(self,age,sex,height,weight):
		self.__age = age
		self.__sex = sex
		self.__height = height
		self.__weight = weight
	def setname(self,name):
		self.name = name
	def show(self):
		print(self.name)
		print(self.__age)
		print(self.__sex)
		print(self.__height)
		print(self.__weight)
class student(human):
	__classes = 0
	__grade = 0
	__num = 0
	def __init__(self,classes,grade,num,age,sex,height,weight):
		self.__classes = classes
		self.__grade = grade
		self.__num = num
		human.__init__(self,age,sex,height,weight)
	def show(self):
		human.show(self)
		print(self.__classes)
		print(self.__grade)
		print(self.__num)
		
if __name__ == '__main__':

	#c =C()
	#c.showall()
	#c.setnum(3)
	#c.show()
	#c.setname('D')
	#c.showall()
	
	a = student(12,3,20070305,19,'male',175,65)
	a.setname('Tom')
	a.show()
		