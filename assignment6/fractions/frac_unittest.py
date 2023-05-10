import unittest
from frac import Frac 
from frac import MixedFrac
from unittest import mock

class UnitTest(unittest.TestCase):
	"""
	Unit Tests
	"""
	@mock.patch('builtins.input', return_value='2460000 98400')
	def test1(self, mocked_input): 
		expected_output = "25 0 / 98400"
		mocked_input = input()
		splitInput = mocked_input.split()
		numerator = int(splitInput[0])
		denominator = int(splitInput[1])
		
		frac = Frac(numerator, denominator)
		mixedFrac = MixedFrac(frac)
		mixedFrac.calculateWholeNumber()

		with mock.patch('builtins.print') as mocked_print:
			mixedFrac.printMixedFrac()
			mocked_print.assert_called_with(expected_output)
	
	@mock.patch('builtins.input', return_value='27 12')
	def test2(self, input):
		expected_output = "2 3 / 12"
		mocked_input = input()
		splitInput = mocked_input.split()
		numerator = int(splitInput[0])
		denominator = int(splitInput[1])
		
		frac = Frac(numerator, denominator)
		mixedFrac = MixedFrac(frac)
		mixedFrac.calculateWholeNumber()

		with mock.patch('builtins.print') as mocked_print:
			mixedFrac.printMixedFrac()
			mocked_print.assert_called_with(expected_output)



if __name__ == "__main__":
	unittest.main()