import math
class Circle:
	def __init__(self , r):
		self.r = r
	def area(self):
		a = ((self.r*self.r)* math.pi)
		print (a)
	def Perimeter(self):
		b = ((self.r*2)* math.pi)
		print (b)
s1 = Circle(2.5)
s1.area()
s1.Perimeter()