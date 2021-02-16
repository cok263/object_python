class Point:

#Атрибут класса(статическая переменная, также может быть приватной, т.е. __count и иметь геттеры и сеттеры)
	count = 0

# _x - условно приватная переменная(просто говорит о том, что ее извне напрямую менять не стоит, хотя такая возможность имеется)
# __x - приватная переменная, не поменять извне напрямую
	def __init__(self, x, y):
		self.__x = x
		self.__y = y
		Point.count += 1

#Класс-метод
	@classmethod
	def class_count(cls):
		print(f'Количество точек(класс-метод): {cls.count}')

#Статический метод. Разница только в том, что статический метод автоматически передает имя класса
	@staticmethod
	def static_count():
		print(f'Количество точек(статический): {Point.count}')



#2 вида описания свойств
	def get_x(self):
		return self.__x

	def set_x(self, value):
		self.__x = value

	x = property(get_x, set_x)


	@property
	def y(self):
		return self.__y
	
	@y.setter
	def y(self, value):
		self.__y = value
#

	def move_to(self, x, y):
		self.__x = x
		self.__y = y


	def move_by(self, x, y):
		self.__x += x
		self.__y += y

	def __repr__(self):
		return f'Я - точка: {self.__x} x {self.__y}'


def main():
	point = Point(10, 20)
	print(point)
	point.move_to(100, 200)
	print(point.x, ' : ', point.y)
	point.move_by(10, 20)
	print(point.x, ' : ', point.y)
	point.x = 30
	point.y = 40
	print(point)
	Point.class_count()
	point2 = Point(22, 33)
	Point.static_count()
	point3 = Point(33, 44)
	print(f'Количество точек: {Point.count}')



if __name__ == '__main__':
	main()