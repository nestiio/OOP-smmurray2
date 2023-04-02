from hypothesis import given, strategies as st
from fractions import Fraction
from frac import MixedFrac
from frac import Frac
import unittest
from math import floor

class TestFractions(unittest.TestCase):
	@given(st.fractions())
	def test_ratios_equal(self, f):
		frac = Frac(f.numerator, f.denominator)
		fractionRatio = f.numerator / f.denominator
		
		fracRatio = frac.getNumerator() / frac.getDenominator()
		assert fracRatio == fractionRatio

	@given(st.fractions(min_value=1))
	def test_whole_number(self, f):
		frac = Frac(f.numerator, f.denominator)
		mixedFrac = MixedFrac(frac)
		mixedFrac.calculateWholeNumber()

		mixedFracWholeNumber = mixedFrac.getWholeNumber()
		fractionWholeNumber = floor(f)
		assert mixedFracWholeNumber == fractionWholeNumber

if __name__ == "__main__":
    unittest.main()