'''
Непряме наслідування
'''

class A:
	def method(self):
		print("A method")
	
class B(A):
	def another_method(self):
		print("B method")
	
class C(B):
	def third_method(self):
		print("C method")
	
c = C()
c.method()
c.another_method()
c.third_method()

'''
Ф-ція наслідуваннч super, яка вказує на батьківський клас. Для пошуку методу по його імені у суперкласі об'єкту.
'''

class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    super().spam()
# super().spam() вызывает метод суперкласса spam.           
B().spam()
