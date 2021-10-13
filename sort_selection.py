#selection_sort
import unittest
from typing import List

def selection_sort(list_to_sort: List) -> List:
    
    list_len = len(list_to_sort)
    
    is_sorted = True
    
    for i in range(list_len):
        min_item_id = i
        
        for j in range(i, list_len):
            if(list_to_sort[min_item_id] > list_to_sort[j]):
                min_item_id = j
                is_sorted = False
                
        if(is_sorted == True):
            return list_to_sort
        
        list_to_sort[i], list_to_sort[min_item_id] = list_to_sort[min_item_id], list_to_sort[i] 
        
    
    return list_to_sort
        
class MyTest(unittest.TestCase):
    
    def test_selection_sort(self):
        self.assertEqual(selection_sort([4, 7, 2, 5, 3, 4, 4]), [2, 3, 4, 4, 4, 5, 7])
        
if __name__ == '__main__':
    unittest.main()
