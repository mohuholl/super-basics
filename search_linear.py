#linear_search
import unittest
from typing import List, Optional 

def linear_search(find_this, items_list: List) -> Optional[int]:
    
    for index in range(len(items_list)):
        if(find_this == items_list[index]):
            return index
    
    return None

class MyTest(unittest.TestCase):
    
    def test_linear_search(self):
        self.assertEqual(linear_search(777,[4,5,333,6,5,777,865,12,33,4,5,6,1,2]),5)
        
    def test_linear_search_none(self):
        self.assertEqual(linear_search('100',[4,5,333,6,5,777,865,12,33,4,5,6,1,2]),None)
        
if __name__ == '__main__':
    unittest.main()