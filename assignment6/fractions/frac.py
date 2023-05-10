class Frac:
    def __init__(self, numerator:int, denominator:int) -> None:
        """
        Constructor for the class Frac
        """
        self.__numerator = numerator
        self.__denominator = denominator

    def setNumerator(self, newNumerator:int) -> None:
        """
        Set function for the numerator
        """
        self.__numerator = newNumerator

    def getNumerator(self) -> int:
        """
        Get function for the numerator
        """
        return self.__numerator
    
    def setDenominator(self, newDenominator:int) -> None:
        """
        Set function for the denominator
        """
        self.__denominator = newDenominator

    def getDenominator(self) -> int:
        """
        Get function for the denominator
        """
        return self.__denominator
    
    def printFrac(self) -> None:
        """
        Print function for fraction data type
        """
        print(f"{self.__numerator} / {self.__denominator}")


class MixedFrac(Frac):
    def __init__(self, fraction:Frac) -> None:
        """
        Constructor for the class MixedFrac
        """
        self.__fraction = fraction
        self.__wholeNumber = 0

    def setWholeNumber(self, wholeNumber:int) -> None:
        """
        Set function for the whole number
        """
        self.__wholeNumber = wholeNumber

    def getWholeNumber(self) -> int:
        """
        Get function for the numerator
        """
        return self.__wholeNumber
    
    def setFrac(self, fraction:Frac) -> None:
        """
        Set function for the fraction
        """
        self.__fraction = fraction
    
    def getFrac(self) -> Frac:
        """
        Get function for the fraction
        """
        return self.__fraction
    
    def calculateWholeNumber(self) -> None:
        """
        Calculate mixed fraction
        """
        self.__wholeNumber = self.__fraction.getNumerator() // self.__fraction.getDenominator()
        self.__fraction.setNumerator(self.__fraction.getNumerator() % self.__fraction.getDenominator()) 
    
    def printMixedFrac(self) -> None:
        """
        Print function for the fraction
        """
        print(f'{self.__wholeNumber} {self.__fraction.getNumerator()} / {self.__fraction.getDenominator()}')


