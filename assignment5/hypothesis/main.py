from classes import TitleCost
from classes import ComparisonClass

def main() -> None:
	inputString = input()
	splitInput = inputString.split()
	cap = float(splitInput[1])
	title = splitInput[0]
	
	titlecost = TitleCost(title)
	comparison = ComparisonClass(titlecost, cap)

	minimum = comparison.getMin()
	print (str(minimum))
	

if __name__ == "__main__":
	main()