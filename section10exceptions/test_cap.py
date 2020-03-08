'''
    Simple example of using unittest for Python
'''
import unittest
import cap

class TestCap(unittest.TestCase):
    '''
        Unit test for the capitalization function
    '''
    def test_one_word(self):
        '''
        Test a single work is capitalized
        '''
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_two_words(self):
        '''
        Test both words of a two word string are capitalized
        '''
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()
    