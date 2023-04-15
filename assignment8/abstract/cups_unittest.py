import unittest
from unittest import mock
from cups import CupDiameter
from cups import CupRadius
from cups import CupList


class UnitTest(unittest.TestCase):

	def test1(self):
		expected_output = "bluegreenred"
		cupList = CupList()
		with mock.patch('builtins.input', return_value='red 10'): # color radius
			inp = input().split()
			cupList.append(CupRadius(inp[0], int(inp[1])))
		with mock.patch('builtins.input', return_value='10 blue'): # diameter color
			inp = input().split()
			cupList.append(CupDiameter(inp[1], int(inp[0])))
		with mock.patch('builtins.input', return_value='green 7'): # color radius
			inp = input().split()
			cupList.append(CupRadius(inp[0], int(inp[1])))
		cupList.sort()

		with mock.patch('builtins.print') as mocked_print:
			actual_output = ""
			for i in range(len(cupList)):
				actual_output += cupList[i].getColor()
			print(actual_output)
			mocked_print.assert_called_with(expected_output)

	def test2(self):
		expected_output = "greenblueyellow"
		cupList = CupList()
		with mock.patch('builtins.input', return_value='12 yellow'): # diameter color
			inp = input().split() # inp = ['12', 'yellow'] ;  inp[0] = '12' ; inp[1] = 'yellow'
			cupList.append(CupDiameter(inp[1], int(inp[0]))) #CupDiameter(str, int)
		with mock.patch('builtins.input', return_value='10 blue'): # diameter color
			inp = input().split()
			cupList.append(CupDiameter(inp[1], int(inp[0])))
		with mock.patch('builtins.input', return_value='8 green'): # diameter color
			inp = input().split()
			cupList.append(CupDiameter(inp[1], int(inp[0])))
		cupList.sort()

		with mock.patch('builtins.print') as mocked_print:
			actual_output = ""
			for i in range(len(cupList)):
				actual_output += cupList[i].getColor()
			print(actual_output)
			mocked_print.assert_called_with(expected_output)

	def test3(self):
		expected_output = "purplecyanpink"
		cupList = CupList()
		with mock.patch('builtins.input', return_value='pink 13'): # color radius
			inp = input().split()
			cupList.append(CupRadius(inp[0], int(inp[1])))
		with mock.patch('builtins.input', return_value='cyan 12'): # color radius
			inp = input().split()
			cupList.append(CupRadius(inp[0], int(inp[1])))
		with mock.patch('builtins.input', return_value='purple 7'): # color radius
			inp = input().split()
			cupList.append(CupRadius(inp[0], int(inp[1])))
		cupList.sort()

		with mock.patch('builtins.print') as mocked_print:
			actual_output = ""
			for i in range(len(cupList)):
				actual_output += cupList[i].getColor()
			print(actual_output)
			mocked_print.assert_called_with(expected_output)

if __name__ == "__main__":
	unittest.main()