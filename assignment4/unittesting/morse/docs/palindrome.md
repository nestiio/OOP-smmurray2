Module palindrome
=================
A program for converting strings into morse code and finding if it's a palindrome

Classes
-------

`Morse(text: str)`
:   Morse code
    
    Constructor

    ### Ancestors (in MRO)

    * palindrome.Text

    ### Methods

    `getCode(self) ‑> str`
    :   Gets morse

    `isPalindrome(self) ‑> str`
    :   Checks if the translated text is in fact a palindrome

    `setCode(self) ‑> None`
    :   Sets morse

`Text(text: str)`
:   Text Class
    
    Constructor

    ### Descendants

    * palindrome.Morse

    ### Methods

    `getText(self) ‑> str`
    :   Gets text

    `setText(self, text: str) ‑> None`
    :   Sets text

    `translate(self) ‑> str`
    :   Translates text into morse code and saves that into 'morse' string