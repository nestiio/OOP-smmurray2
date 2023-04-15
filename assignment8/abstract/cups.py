from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Union, List, overload, Iterable
import collections

class KattisCup(ABC):
	"""
	Solution ABC class for Kattis problems
	"""
	def __init__(self, color:Any, number:Any) -> None:
		"""
		Constructor
		:param data_source: input data source object
		:return: None
		"""
		pass

	@abstractmethod
	def getColor(self) -> str:
		"""
		Getter function for color
		"""
		pass

	@abstractmethod
	def setColor(self, newColor:str) -> None:
		"""
		Setter function for color
		"""
		pass

	@abstractmethod
	def getRadius(self) -> int:
		"""
		Getter function for radius
		"""
		pass

	@abstractmethod
	def setRadius(self, newRadius:int) -> None:
		"""
		Setter function for radius
		"""
		pass

	@abstractmethod
	def __lt__(self, other:Any) -> bool:
		"""
		Less than operator
		"""
		pass

class CupDiameter(KattisCup):
	def __init__(self, color:str, diameter:int) -> None:
		"""
		Constructor for CupDiameter
		"""
		self.__color:str = color
		self.__radius:int = diameter // 2
        
	def getColor(self) -> str:
		"""
		Getter function for color
		"""
		return self.__color
	
	def setColor(self, newColor:str) -> None:
		"""
		Setter function for color
		"""
		self.__color = newColor

	def getRadius(self) -> int:
		"""
		Getter function for radius
		"""
		return self.__radius
	
	def setRadius(self, newRadius:int) -> None:
		"""
		Setter function for radius
		"""
		self.__radius = newRadius

	def __lt__(self, other:Union[CupDiameter, CupRadius]) -> bool:
		"""
		Overloading less than operator, to help with sorting
		"""
		return self.__radius < other.getRadius()

class CupRadius(KattisCup):
	def __init__(self, color:str, radius:int):
		"""
		Constructor for CupRadius
		"""
		self.__color:str = color
		self.__radius:int = radius
	
	def getColor(self) -> str:
		"""
		Getter function for color
		"""
		return self.__color
	
	def setColor(self, newColor:str) -> None:
		"""
		Setter function for color
		"""
		self.__color = newColor

	def getRadius(self) -> int:
		"""
		Getter function for radius
		"""
		return self.__radius
	
	def setRadius(self, newRadius:int) -> None:
		"""
		Setter function for radius
		"""
		self.__radius = newRadius

	def __lt__(self, other:Union[CupDiameter, CupRadius]) -> bool:
		"""
		Overloading less than operator, to help with sorting
		"""
		return self.__radius < other.getRadius()

class CupList(collections.abc.MutableSequence[Union[CupDiameter, CupRadius]]):
	def __init__(self) -> None:
		"""
		Constructor for CupList
		"""
		self.__data:List[Union[CupDiameter, CupRadius]] = []
	@overload
	def __getitem__(self, index:int) -> Union[CupDiameter, CupRadius]:
		"""
		Returns cup at the specified index
		"""
		return self.__data[index]
	
	@overload # mypy does not like that these were not overloaded, behavior of this doesn't matter as it is not used
	def __getitem__(self, index:slice) -> List[Union[CupDiameter, CupRadius]]:
		return self.__data[index]

	def __getitem__(self, index:Union[int, slice]) -> Any:
		return self.__data[index]
	
	@overload
	def __setitem__(self, index:int, cup:Union[CupDiameter, CupRadius]) -> None:
		"""
		Sets the item at an index to whatever is passed to the function
		"""
		self.__data[index] = cup

	@overload
	def __setitem__(self, index:slice, cups:Iterable[Union[CupDiameter, CupRadius]]) -> None:
		self.__data[index] = cups

	def __setitem__(self, index:Union[int, slice], cup:Any) -> None:
		self.__data[index] = cup
	
	@overload
	def __delitem__(self, index:int) -> None:
		"""
		Deletes an item from the list
		"""
		del self.__data[index]

	@overload
	def __delitem__(self, index:slice) -> None:
		del self.__data[index]
	
	def __delitem__(self, index:Union[int, slice]) -> None:
		del self.__data[index]


	def __len__(self) -> int:
		"""
		Returns the length of the list
		"""
		return len(self.__data)
	
	def insert(self, index:int, cup:Union[CupDiameter, CupRadius]) -> None:
		"""
		Inserts an item into the list
		"""
		self.__data.insert(index, cup)

	def append(self, cup:Union[CupDiameter, CupRadius]) -> None:
		"""
		Appends an item to the end of the list
		"""
		self.__data.append(cup)

	def sort(self) -> None:
		"""
		Sort the list
		"""
		self.__data.sort()
