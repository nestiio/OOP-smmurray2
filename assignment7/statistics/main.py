from stats import Stats
from stats import Nums
from typing import List
def main() -> None:
	"""
	Main
	"""
	stats:List[Stats] = []
	numsList:List[int] = []
	case:int = 1

	while (True):
		try: 
			inp:str = input()
			splitIn:List[str] = inp.split()
			for i in range(len(splitIn) - 1): # get list of numbers excluding the first one
				numsList.append(int(splitIn[i + 1]))
			nums:Nums = Nums(len(numsList), numsList)
			stats.append(Stats(nums, case))
			case += 1
			numsList = []
		except EOFError as e:
			break
		
		
	for i in range(len(stats)): # output
		stats[i].printStats()


if __name__ == "__main__":
    main()