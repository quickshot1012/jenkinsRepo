import unittest
import foo

class TestBar(unittest.TestCase):

    def testOutput(self):
        self.assertEqual(foo.bar(), 'bar')

if __name__ == '__main__':
    unittest.main()
