import unittest
from hypothesis import strategies as st, given
from classes import TitleCost
from classes import ComparisonClass

class HypothesisTesting(unittest.TestCase):
	@given(st.floats(min_value=0, max_value=100))
	def test1(self, floats:float):
		testTitle1 = "GoneWithTheWind"
		titlecost = TitleCost(testTitle1)
		comparison = ComparisonClass(titlecost, floats)
		minimum = comparison.getMin()
        
		assert(minimum == min(float(len(testTitle1)), floats))
	
	@given(st.floats(min_value=0, max_value=100))
	def test2(self, floats:float):
		testTitle2 = "Gigi"
		titlecost = TitleCost(testTitle2)
		comparison = ComparisonClass(titlecost, floats)
		minimum = comparison.getMin()
        
		assert(minimum == min(float(len(testTitle2)), floats))


if __name__ == "__main__":
    unittest.main()