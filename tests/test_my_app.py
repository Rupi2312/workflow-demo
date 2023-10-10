import unittest
from my_app import add
class TestMyApp(unittest.TestCase):
   def test_add(self):
       self.assertEqual(add(1,2),3)
   def test_add_negative_numbers(self):
       self.assertEqual(add(-1,-2),-3)

if __name__ == '__main__':
    unittest.main()
