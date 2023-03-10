from palindrome import Morse
import unittest

class MorseTest(unittest.TestCase):
    """"
    Unit Tests
    """

    def test1(self):
        input1 = "159"
        self.assertEqual(Morse(input1).isPalindrome(), "1", "Test failed...")

    def test2(self):
        input2 = "A E"
        self.assertEqual(Morse(input2).isPalindrome(), "1", "Test failed...")

    def test3(self):
        input3 = "Hello Darkness My Old Friend"
        self.assertEqual(Morse(input3).isPalindrome(), "0", "Test failed...")
  
def main():
	test = MorseTest()
	test.test1()
	test.test2()
	test.test3()

if __name__ == "__main__":
    main()
