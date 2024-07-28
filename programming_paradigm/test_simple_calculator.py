import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test cases for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test.
        This method is called before each test method is executed.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the addition method.
        Verify that the add method returns correct results for various inputs.
        """
        # Test with positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test with a negative number
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Test with zero values
        self.assertEqual(self.calc.add(0, 0), 0)
        # Test with negative numbers
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_subtraction(self):
        """
        Test the subtraction method.
        Verify that the subtract method returns correct results for various inputs.
        """
        # Test with positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test with a negative number
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        # Test with zero values
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Test with negative numbers
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    def test_multiplication(self):
        """
        Test the multiplication method.
        Verify that the multiply method returns correct results for various inputs.
        """
        # Test with positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test with a negative number
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        # Test with zero values
        self.assertEqual(self.calc.multiply(0, 0), 0)
        # Test with negative numbers
        self.assertEqual(self.calc.multiply(-5, -5), 25)

    def test_division(self):
        """
        Test the division method.
        Verify that the divide method returns correct results for various inputs,
        including handling division by zero.
        """
        # Test with positive numbers
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Test with a negative number
        self.assertEqual(self.calc.divide(-10, 2), -5)
        # Test with zero numerator
        self.assertEqual(self.calc.divide(0, 1), 0)
        # Test with negative numbers
        self.assertEqual(self.calc.divide(-10, -2), 5)
        # Test division by zero, should return None
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == '__main__':
    # Run the tests when this script is executed directly
    unittest.main()
