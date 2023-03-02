from polygon import Polygon

"""
Main
"""
def main() -> None:
	"""
	Main function
	- Checks number of polygons based on first user input, then creates a polygon for each one
	"""
	poly = []
	x = int(input())
	for i in range(x):
		numbers = map(int, input().split())
		points = []
		count = 0
		for j in numbers:
			if count == 0:
				n = j
			else:
				points.append(j)
			count += 1
		poly.append(Polygon(n, points))


	for i in range(len(poly)):
		print (str(poly[i].area()))

if __name__ == "__main__":
    main()
