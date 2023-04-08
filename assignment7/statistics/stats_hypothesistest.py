from hypothesis import given, strategies as st
from stats import Nums
from stats import Stats
import unittest

class TestStats(unittest.TestCase):
	@given(st.lists(st.integers(), min_size=1, max_size=10))
	def testMinCalculation(self, list):
		length = len(list)
		nums = Nums(length, list)
		stats = Stats(nums, 0) # case number can be anything, so send 0
		assert min(list) == stats.getMin()
	
	@given(st.lists(st.integers(), min_size=1, max_size=10))
	def testMaxCalculation(self, list):
		length = len(list)
		nums = Nums(length, list)
		stats = Stats(nums, 0) # case number can be anything, so send 0
		assert max(list) == stats.getMax()


if __name__ == "__main__":
	unittest.main()
