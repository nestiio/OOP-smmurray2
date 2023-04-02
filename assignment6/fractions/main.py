from frac import MixedFrac
from frac import Frac

def main() -> None:
	"""
	Main
	"""
	# input will take a whole line from stdin
	# the input itself will be in the form of a string
	numbers = input()
	while (numbers != "0 0"):
		# convert to numbers then input
		numerator, denominator = map(int, numbers.split())
		
		frac = Frac(numerator, denominator)
		mixedFrac = MixedFrac(frac)
		mixedFrac.calculateWholeNumber()
		mixedFrac.printMixedFrac()

		numbers = input()
        
         
if __name__ == "__main__":
    main()