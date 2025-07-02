from .util import cast_to_int

class Calculator:
	def __init__(self):
		pass

	def add(self,num_1, num_2):
		return num_1

	def div(num_1, num_2):
		return num_1/num_2

	def mul(self,num_1, num_2):
		return num_1 * num_2
	
	def function(self, num_1, num_2):
		return num_1 + num_2*num_1/num_2

	def power(num_1, num_2):
		return num_1^num_2
	
	def function(num_1,num_2):
		return 0

if __name__ == "__main__":
	calc = Calculator()
	calc.add(2, 2)
	calc.div(4, 2)
