#from palindrome import Palindrome
from palindrome import Morse

def main() -> None:
    """
    Main
    """
    text = input().upper()
    code = Morse(text)

    code.isPalindrome()
    
if __name__ == "__main__":
    main()
