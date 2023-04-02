import unittest
from frac import Frac 
from frac import MixedFrac
from unittest import mock

class UnitTest(unittest.TestCase):
	"""
	Unit Tests
	"""
	@mock.patch('builtins.input', return_value='27 12')
	def test1(self, input): 
		expected_output = "25 0 / 98400"
		numerator, denominator = map(int, input.split())
		
		frac = Frac(numerator, denominator)
		mixedFrac = MixedFrac(frac)
		mixedFrac.calculateWholeNumber()
		mixedFrac.printMixedFrac()
	
	@mock.patch('builtins.input', lambda _: '27 12')
	def test2(self, input):
		numerator, denominator = map(int, input.split())
		frac = Frac(numerator, denominator)
		mixedFrac = MixedFrac(frac)
		mixedFrac.calculateWholeNumber()

		with mock.patch('builtins.print') as mocked_print:
			mixedFrac.printMixedFrac()
			mocked_print.assert_called_with('2 ', '3 / 12')
	
	def test3(self):
		somethingelse = 365

def main():
	test = UnitTest()
	test.test1()
	test.test2()


if __name__ == "__main__":
	unittest.main()