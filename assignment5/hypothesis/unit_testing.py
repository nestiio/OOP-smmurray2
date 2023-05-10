import unittest
from unittest import mock
from classes import TitleCost
from classes import ComparisonClass

class UnitTesting(unittest.TestCase):
	@mock.patch('builtins.input', return_value="GoneWithTheWind 13.341")
	def test1(self, mocked_input):
		expected_output = "13.341"
		mocked_input = input()
		splitInput = mocked_input.split()
		titlecost = TitleCost(splitInput[0])
		comparison = ComparisonClass(titlecost, float(splitInput[1]))

		minimum = comparison.getMin()
		with mock.patch('builtins.print') as mocked_print:
			print (str(minimum))
			mocked_print.assert_called_with(expected_output)

	
	@mock.patch('builtins.input', return_value="Gigi 93.7")
	def test2(self, mocked_input):
		expected_output = "4.0"
		mocked_input = input()
		splitInput = mocked_input.split()
		titlecost = TitleCost(splitInput[0])
		comparison = ComparisonClass(titlecost, float(splitInput[1]))

		minimum = comparison.getMin()
		with mock.patch('builtins.print') as mocked_print:
			print (str(minimum))
			mocked_print.assert_called_with(expected_output)

if __name__ == "__main__":
    unittest.main()