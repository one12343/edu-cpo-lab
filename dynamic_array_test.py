import unittest
from hypothesis import given, settings
import hypothesis.strategies as st
from dynamic_array import *
import math

class TestMutableULList(unittest.TestCase):
    # first we use unit test!

    def test_api(self):

        # print('\nTesting cons...')
        array = Dynamic_array()
        l1 = cons(None, cons(1, array))
        l2 = cons(1, cons(None, array))
        l3 = cons([3,2], cons(None, array))
        self.assertEqual(str(array), "[]")
        self.assertEqual(str(l1), "[None, 1]")
        self.assertEqual(str(l2), "[1, None]")
        self.assertNotEqual(str(array), str(l1))
        self.assertNotEqual(str(array), str(l2))
        self.assertNotEqual(str(l1), str(l2))
        self.assertEqual(str(l1), str(cons(None, cons(1, array))))
        self.assertEqual(str(l3), "[3, 2, None]")


        # print('\nTesting length...')
        self.assertEqual(get_len(array), 0)
        self.assertEqual(get_len(l1), 2)
        self.assertEqual(get_len(l2), 2)

        # print('\nTesting remove...')
        self.assertEqual(get_array(remove_index(l1, 0)), [1])
        self.assertEqual(get_array(remove_index(l1, 1)), [None])
        array2 = Dynamic_array()
        temp_list = [1, 2, 3, 4, 5, 6]
        for i in temp_list:
            array2=append(array2,i)
        self.assertEqual(get_array(remove_value(array2, 3)), [1,2,4,5,6])
        self.assertEqual(get_array(remove_value(array2, 5)), [1,2,3,4,6])

        # print('\nTesting member...')
        self.assertFalse(member(None, array))
        self.assertTrue(member(None, l1))
        self.assertTrue(member(1, l1))
        self.assertFalse(member(2, l1))

        # print('\nTesting reverse...')
        self.assertEqual(l1, reverse_arr(l2))
        temp_list_reverse=[6,5,4,3,2,1]
        array5 = Dynamic_array()
        array6 = Dynamic_array()
        for i in temp_list:
            array5 = append(array5, i)
        for i in temp_list_reverse:
            array6 = append(array6, i)
        self.assertEqual(array6, reverse_arr(array5))

        # print('\nTesting to_list and from_list...')
        self.assertEqual(to_list(l1), [None, 1])
        self.assertEqual(l1, from_list([None, 1]))

        # print('\nTesting concat...')
        self.assertEqual(concat(l1, l2), from_list([None, 1, 1, None]))

        # print('\nTesting append and getitem...')
        buf = []
        for e in l1:
            buf.append(e)
        self.assertEqual(buf, [None, 1])
        lst = to_list(l1) + to_list(l2)
        for e in l1:
            lst.remove(e)
        for e in l2:
            lst.remove(e)
        self.assertEqual(lst, [])


        array = Dynamic_array()
        temp_list=[1,2,3,4,5,6]
        for i in temp_list:
            array=append(array,i)
        get_a=get_array(array)
        self.assertEqual(get_a, temp_list)
        temp1=get_item(array,2)
        self.assertEqual(temp1, temp_list[2])
        temp1 = get_item(array, 5)
        self.assertEqual(temp1, temp_list[5])

        # print('\nRewrite_eq and test eq...')
        array3 = Dynamic_array()
        array4 = Dynamic_array()
        self.assertEqual(array3, array4)
        for i in temp_list:
            array3 = append(array3,i)
            array4 = append(array4, i)
        self.assertEqual(array3, array4)

        # print('\nTest_change_value...')
        array3[3]=0
        self.assertEqual(str(array3), "[1, 2, 3, 0, 5, 6]")

        # print('\nTest_filter...')
        array=Dynamic_array()
        temp_list=[1, 4, 6, 7, 9, 12, 17]
        for i in temp_list:
            array = append(array,i)
        temp1=filter(array,is_odd)  #(array,function)
        self.assertEqual(str(temp1), "[1, 7, 9, 17]")

        array = Dynamic_array()
        temp_list = ['test', None, '', 'str', ' ', 'END']
        for i in temp_list:
            array = append(array, i)
        temp2 = filter(array, is_not_empty)  # (array,function)
        self.assertEqual(str(temp2), "['test', 'str', 'END']")

        array = Dynamic_array()
        temp_list = [1,2,3,2,5,2,7,2,9]
        for i in temp_list:
            array = append(array, i)
        temp3 = filter(array, remove_value_2)  # (array,function)
        self.assertEqual(str(temp3), "[1, 3, 5, 7, 9]")

        array = Dynamic_array()
        for i in range(1,101):
            array = append(array,i)
        temp4 = filter(array, is_sqr)  # (array,function)
        self.assertEqual(str(temp4), "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]")

        # print('\nTest_map...')
        array=Dynamic_array()
        temp_list=[2,3,4,5,6,7,8,9]
        for i in temp_list:
            array = append(array, i)
        temp=map(array,my_square)
        self.assertEqual(str(temp), "[4, 9, 16, 25, 36, 49, 64, 81]")

        temp2 = map(temp, my_sqr)
        self.assertEqual(str(temp2), str(temp_list))  #[2,3,4,5,6,7,8,9]

        # print('\nTest_reduce...')
        array = Dynamic_array()
        temp_list=[1, 2, 3, 4, 5]
        for i in temp_list:
            array = append(array, i)
        result = reduce(array, my_add)
        self.assertEqual(str(result), "15")

        # print('\nTest_empty...')
        array = Dynamic_array()
        self.assertEqual(empty(array), True)
        array=append(array,1)
        self.assertEqual(empty(array), False)
        array=remove_value(array,1)
        self.assertTrue(empty(array))
        array = append(array, 2)
        self.assertFalse(empty(array))

# print('\nThese are functions to test filter')
def is_odd(x):
    return x % 2 == 1

#Delete None or empty string
def is_not_empty(s):
    if s!=None:
        return (len(s.strip()) > 0)
    return (s!=None )

#Filter out the number whose square root is an integer in 1 ~ 100
def is_sqr(x):
    return math.sqrt(x) % 1 == 0

def remove_value_2(x):
    return x!=2


# print('\nThese are functions to test map')
def my_square(n):
    return n * n

def my_sqr(x):
    return int(math.sqrt(x))

# print('\nTest of function of reduce')
def my_add(x,y):
    return x+y

if __name__ == '__main__':
    unittest.main()
