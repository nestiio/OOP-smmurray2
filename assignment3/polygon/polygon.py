from typing import List

"""
Program for finding the area of convex polygons
"""

class Point:
	"""
	Point Class
	"""
	def __init__(self, x:int, y:int) -> None:
		"""
		Constructor
		"""
		self.__x = x
		self.__y = y

	def setX(self, x:int) -> None:
		"""
		Sets x coordinate
		"""
		self.__x = x
        
	def setY(self, y:int) -> None:
		"""
		Sets y coordinate
		"""
		self.__y = y
    
	def getX(self) -> int:
		"""
		Gets x coordinate
		"""
		return self.__x
    
	def getY(self) -> int:
		"""
		Gets y coordinate
		"""
		return self.__y

class Polygon(Point):
	"""
	Polygon Class
	- Inherits from point class
	- Size of points array must be even
	"""
	def __init__(self, numPoints:int, points:List[int]) -> None:
		"""
		Constructor
		"""
		self.__numPoints = numPoints
		self.__points = []
		for i in range(0, numPoints*2, 2):
			self.__points.append(Point(points[i], points[i+1]))

    
	def area(self) -> float:
		"""
		Finds the area of one convex polygon at a time
		- has an edge case for when i+1 goes past n
		"""
		area = 0.0
		for i in range(self.__numPoints):
			if i+1 < self.__numPoints: 
				pointOne = self.__points[i]
				pointTwo = self.__points[i+1]
			else: # edge case where i+1 goes past n
				pointOne = self.__points[i]
				pointTwo = self.__points[0]

			area += (pointOne.getX() * pointTwo.getY() - pointTwo.getX() * pointOne.getY())
		
		area = abs(area)
		area *= 0.5
		return float(area)
	
	def setPoints(self, points:List[Point]) -> None:
		"""
		Sets points
		"""
		self.__points = points
	
	def getPoints(self) -> List[Point]:
		"""
		Gets points
		"""
		return self.__points
	
	def setNumPoints(self, numPoints:int) -> None:
		"""
		Sets the number of points
		"""
		self.__numPoints = numPoints
	
	def getNumPoints(self) -> int:
		"""
		Gets the number of points
		"""
		return self.__numPoints
