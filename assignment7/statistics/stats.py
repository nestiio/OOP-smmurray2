from typing import List

"""
A program that analyzes given samples of data and returns the minimum, maximum, and range of the values
"""

class Nums:
	"""
	Nums Class
	"""
	def __init__(self, numNumbers:int, numbers:List[int]) -> None:
		"""
		Constructor
		"""
		self.__numNumbers = numNumbers
		self.__numbers = numbers
	
	def setNumNumbers(self, min:int) -> None:
		"""
		Sets min
		"""
		self.__numNumbers = min
	
	def setNumbers(self, numbers:List[int]) -> None:
		"""
		Sets max
		"""
		self.__numbers = numbers

	def getNumNumbers(self) -> int:
		"""
		Gets min
		"""
		return self.__numNumbers
	
	def getNumbers(self) -> List[int]:
		"""
		Gets max
		"""
		return self.__numbers

class Stats(Nums):
	def __init__(self, nums:Nums, case:int) -> None:
		"""
		Constructor
		"""
		self.__nums = nums
		self.__case = case

	def setNums(self, nums:Nums) -> None:
		"""
		Sets nums
		"""
		self.__nums = nums
	
	def setCase(self, case:int) -> None:
		"""
		Sets case
		"""
		self.__case = case

	def getNums(self) -> Nums:
		"""
		Gets nums
		"""
		return self.__nums
	
	def getCase(self) -> int:
		"""
		Gets case number
		"""
		return self.__case
	def getMin(self) -> int:
		"""
		Calculates and returns min
		"""
		numbers = self.__nums.getNumbers()

		if (len(numbers) != 0):
			min = numbers[0]
		else:
			min = 0
		
		for i in numbers:
			if min > i:
				min = i

		return min
	
	def getMax(self) -> int:
		"""
		Calculates and returns max
		"""
		numbers = self.__nums.getNumbers()

		if (len(numbers) != 0):
			max = numbers[0]
		else:
			max = 0
		
		for i in numbers:
			if max < i:
				max = i

		return max

	def printStats(self) -> None:	
		"""
		Print Function
		"""
		print("Case {}: {} {} {}".format(self.getCase(), self.getMin(), self.getMax(), self.getMax() - self.getMin()))

