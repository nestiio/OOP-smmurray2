import typing

class TitleCost():
	def __init__(self, title:str) -> None:
		"""
		Constructor for the class TitleCost
		"""
		self.__title = title
		self.__cost = float(len(title))
        
	def setTitle(self, newTitle:str) -> None:
		"""
		Setter function for the title data member
		"""
		self.__title = newTitle
	
	def getTitle(self) -> str:
		"""
		Getter function for the title data member
		"""
		return self.__title
    
	def setCost(self, newCost:float) -> None:
		"""
		Setter function for the cost data member
		"""
		self.__cost = newCost
	
	def getCost(self) -> float:
		"""
		Getter function for the cost data member
		"""
		return self.__cost
	
class ComparisonClass():
	def __init__(self, titlecost:TitleCost, cap:float) -> None:
		"""
		Constructor for the class ComparisonClass
		"""
		self.__titlecost = titlecost
		self.__cap = cap

	def setTitleCost(self, newTitleCost:TitleCost) -> None:
		"""
		Setter function for the titlecost data member
		"""
		self.__titlecost = newTitleCost

	def getTitleCost(self) -> TitleCost:
		"""
		Getter function for the titlecost data member
		"""
		return self.__titlecost
	
	def setCap(self, newCap:float) -> None:
		"""
		Setter function for the cap data member
		"""
		self.__cap = newCap

	def getCap(self) -> float:
		"""
		Getter function for the cap data member
		"""
		return self.__cap
	
	def getMin(self) -> float:
		"""
		Function which calculates and returns the minimum between the cost of the title and the cap for the cost
		"""
		return min(self.__cap, self.__titlecost.getCost())