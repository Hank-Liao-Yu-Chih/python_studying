#ch6-1
class book:
	__author = ''
	__name = ''
	__pages = 0
	price = 0
	__press = ''
	#def show(self):
	#	print(self.__author)
	#	print(self.__name)
	def __init__(self,author,name):
		self.__author = author
		self.__name = name
	def __del__(self):
		print("call dell")
	def show(self):
		if self.__check(self.__author):
			print(self.__author)
		else:
			print('No author')
		if self.__check(self.__name):
			print(self.__name)
		else:
			print('No name')
	def setname(self,name):
		self.__name = name
	def setauthor(self,author):
		self.__author = author
	def __check(self,item):
		if item == '':
			return 0
		else:
			return 1
			
class student (book):
	__class = ''
	__grade = ''
	__sname = ''
	def showinfo(self):
		self.show()
			
			
if __name__ == '__main__':
	a = book('Tom','A Wonderfull book')
	#a.author = 'Shane'
	#a.pages = 300
	#a.price = 25
	a.show()
	a.setname("Shane")
	a.setauthor("SONIX")
	a.show()
	
	b = student('Jack','Big Book')
	b.showinfo()
	