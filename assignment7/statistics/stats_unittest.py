import unittest
from stats import Stats
from stats import Nums
from unittest import mock

class UnitTest(unittest.TestCase):
	"""
	Unit Tests
	"""

	def test1(self):
		expected_output = "Case 1: 4 10 6"
		inputList = [2, 4, 10]
		# get nums
		nums = []
		for i in range(1, len(inputList)):
			nums.append(inputList[i])
		
		numsObject = Nums(len(nums), nums)
		statsObject = Stats(numsObject, 1)

		with mock.patch('builtins.print') as mocked_print:
			statsObject.printStats()
			mocked_print.assert_called_with(expected_output)
	
	def test2(self):
		expected_output = "Case 2: 1 9 8"
		inputList = [9, 2, 5, 6, 4, 5, 9, 2, 1, 4]
		# get nums
		nums = []
		for i in range(1, len(inputList)):
			nums.append((inputList[i]))
		
		numsObject = Nums(len(nums), nums)
		statsObject = Stats(numsObject, 2)

		with mock.patch('builtins.print') as mocked_print:
			statsObject.printStats()
			mocked_print.assert_called_with(expected_output)

	def test3(self):
		expected_output = "Case 3: 9 9 0"
		inputList = [1, 9]
		# get nums
		nums = []
		for i in range(1, len(inputList)):
			nums.append(inputList[i])
		
		numsObject = Nums(len(nums), nums)
		statsObject = Stats(numsObject, 3)

		with mock.patch('builtins.print') as mocked_print:
			statsObject.printStats()
			mocked_print.assert_called_with(expected_output)
		

if __name__ == "__main__":
	unittest.main()