import unittest
import maths

class test_algebra(unittest.TestCase):
    """
    Subclass the TestCase class to build these tests.
    New tests must be prefixed with 'test_'
    """
    def test_algebra(self):
        self.assertEqual(maths.add1(1),2)

    def test_circle(self):
        self.assertEqual(maths.circumference(2),12.57)

# To actually... run the tests
if __name__ == '__main__':
    unittest.main()