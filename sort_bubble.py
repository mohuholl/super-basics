#bubble sort
import unittest

def bubble_sort(list_to_sort):
    is_sorted = False
    
    while(is_sorted == False):
        is_sorted = True
        for i in range(len(list_to_sort)-1):
            if(list_to_sort[i]>list_to_sort[i+1]):
                is_sorted = False
                list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]

    return list_to_sort

class MyTest(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([4, 7, 2, 5, 3, 4, 4]), [2, 3, 4, 4, 4, 5, 7])


if __name__ == '__main__':
    unittest.main()