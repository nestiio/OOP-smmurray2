from hypothesis import given, strategies as st
from cups import CupRadius
from cups import CupDiameter
from cups import CupList
import unittest

class HypothesisTesting(unittest.TestCase):
	@given(st.lists(st.integers(), min_size=2, max_size=2))	
	def testLessThan(self, list):
		cupList = CupList()
		cupList.append(CupDiameter("red", list[0]))
		cupList.append(CupRadius("blue", list[1]))

		if list[0] // 2 < list[1]: # list[0] // 2 = radius
			assert cupList[0] < cupList[1]
		elif list[1] < list[0] // 2:
			assert cupList[1] < cupList[0]
	
	@given(st.lists(st.integers(), min_size=10, max_size=10))
	def testSort(self, list):
		cupList = CupList()
		# alternate which class is used
		for i in range(len(list)):
			if i % 2 == 0:
				cupList.append(CupDiameter("red", list[i]))
				list[i] = list[i] // 2 # for checking later
			else:
				cupList.append(CupRadius("blue", list[i]))
		# sort list then compare it to sorted cupList
		list.sort()
		cupList.sort()
		for i in range(len(cupList)):
			assert list[i] == cupList[i].getRadius()

if __name__ == "__main__":
    unittest.main()