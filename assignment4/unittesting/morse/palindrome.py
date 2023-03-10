"""
A program for converting strings into morse code and finding if it's a palindrome
"""

cipher = { 
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        }

class Text:
    """
    Text Class
    """
    def __init__(self, text: str) -> None:
        """
        Constructor
        """
        self.__text = text

    def setText(self, text:str) -> None:
        """
        Sets text
        """
        self.__text = text
    
    def getText(self) -> str:
        """
        Gets text
        """
        return self.__text
    
    def translate(self) -> str:
        """
        Translates text into morse code and saves that into 'morse' string
        """
        code = ""
        for i in self.__text:
            code += cipher.get(i,"") #if it's in the dictionary, return it, else return empty string
        return code
    

class Morse(Text):
    """
    Morse code
    """
    def __init__(self, text:str) -> None:
        newText = Text(text)
        self.__text:Text = newText
        self.__code = self.__text.translate()

    def setCode(self) -> None:
        """
        Sets morse
        """
        self.translate()
    
    def getCode(self) -> str:
        """
        Gets morse
        """
        return self.__code
    
    def isPalindrome(self) -> str:
        """
        Checks if the translated text is in fact a palindrome
        """
        if (len(self.__code) == 0):
            print("0")
            return "0"
        elif (self.__code == self.__code[::-1]):
            print("1")
            return "1"
        else:
            print("0")
            return "0"
