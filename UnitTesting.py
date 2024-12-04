import unittest



class TestList(unittest.TestCase):
    
    def setUp(self):
        """ Is run before each test, thus creating identical test fixtures for each. """
        
        self.emptyList = []  # test fixture
        
    def tearDown(self):
        """ Is run after each test, should any clean up be necessary (like removing 
        files from the filesystem or records from a database)."""
        
        # commented out because the type checker complains about it, even tho it runs fine
        # self.emptyList = None
    
    def testAddToEmpty(self):
        self.assertTrue(len(self.emptyList) == 0)
        self.emptyList.append(1)
        self.assertTrue(len(self.emptyList) == 1)
    
    def testRemoveFromEmpty(self):
        self.assertTrue(len(self.emptyList) == 0)
        self.assertRaises(IndexError, self.emptyList.pop)
        
        
        
if __name__ == "__main__":
    unittest.main()