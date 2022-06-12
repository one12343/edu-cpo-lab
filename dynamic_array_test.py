import unittest
from hypothesis import given
import hypothesis.strategies as st
from dynamic_array import get_len, get_item, reverse_arr, to_list, from_list
from dynamic_array import append, remove_value, remove_index, member, concat
from dynamic_array import get_array, cons, filter, map, reduce, empty
from dynamic_array import Dynamic_array
import math


class TestMutableULList(unittest.TestCase):

    def test_api(self):

        # Testing cons
        array = Dynamic_array()
        l1 = cons(None, cons(1, array))
        l2 = cons(1, cons(None, array))
        l3 = cons([3, 2], cons(None, array))
        self.assertEqual(str(array), "[]")
        self.assertEqual(str(l1), "[None, 1]")
        self.assertEqual(str(l2), "[1, None]")
        self.assertNotEqual(str(array), str(l1))
        self.assertNotEqual(str(array), str(l2))
        self.assertNotEqual(str(l1), str(l2))
        self.assertEqual(str(l1), str(cons(None, cons(1, array))))
        self.assertEqual(str(l3), "[3, 2, None]")

        # Testing length
        self.assertEqual(get_len(array), 0)
        self.assertEqual(get_len(l1), 2)
        self.assertEqual(get_len(l2), 2)

        # Testing remove
        self.assertEqual(get_array(remove_index(l1, 0)), [1])
        self.assertEqual(get_array(remove_index(l1, 1)), [None])

        # Testing member
        self.assertFalse(member(None, array))
        self.assertTrue(member(None, l1))
        self.assertTrue(member(1, l1))
        self.assertFalse(member(2, l1))

        # Testing reverse
        self.assertEqual(l1, reverse_arr(l2))

        # Testing to_list and from_list
        self.assertEqual(to_list(l1), [None, 1])
        self.assertEqual(l1, from_list([None, 1]))

        # Testing concat
        self.assertEqual(concat(l1, l2), from_list([None, 1, 1, None]))

        # Testing append and getitem
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
        temp_list = [1, 2, 3, 4, 5, 6]
        for i in temp_list:
            array = append(array, i)
        get_a = get_array(array)
        self.assertEqual(get_a, temp_list)
        temp1 = get_item(array, 2)
        self.assertEqual(temp1, temp_list[2])
        temp1 = get_item(array, 5)
        self.assertEqual(temp1, temp_list[5])

    def test_cons(self):
        array = Dynamic_array()
        l1 = cons(None, cons(1, array))
        l2 = cons(1, cons(None, array))
        l3 = cons([3, 2], cons(None, array))
        self.assertEqual(str(array), "[]")
        self.assertEqual(str(l1), "[None, 1]")
        self.assertEqual(str(l2), "[1, None]")
        self.assertNotEqual(str(array), str(l1))
        self.assertNotEqual(str(array), str(l2))
        self.assertNotEqual(str(l1), str(l2))
        self.assertEqual(str(l1), str(cons(None, cons(1, array))))
        self.assertEqual(str(l3), "[3, 2, None]")

    def length(self):
        x = [1, 2, 3]
        x2 = [1, 2, 3, 4, 5, 6]
        array = from_list(x)
        array2 = from_list(x2)
        self.assertEqual(get_len(array), 3)
        self.assertEqual(get_len(array2), 6)

    def test_remove(self):
        x = [1, 2, 3]
        array = from_list(x)
        self.assertEqual(get_array(remove_index(array, 0)), [2, 3])
        self.assertEqual(get_array(remove_index(array, 1)), [1, 3])

        x2 = [1, 2, 3, 4, 5, 6]
        array2 = from_list(x2)
        self.assertEqual(get_array(remove_value(array2, 3)), [1, 2, 4, 5, 6])
        self.assertEqual(get_array(remove_value(array2, 5)), [1, 2, 3, 4, 6])

    def test_member(self):
        x = [1, 2, 3, 4, 5, 6]
        array = from_list(x)
        x2 = [1, 2, None, 4, 5, 6]
        array2 = from_list(x2)
        self.assertFalse(member(None, array))
        self.assertTrue(member(None, array2))
        self.assertTrue(member(1, array))
        self.assertFalse(member(3, array2))

    def test_reverse(self):
        x1 = [1, 2, 3, 4, 5, 6]
        x2 = [6, 5, 4, 3, 2, 1]
        array1 = from_list(x1)
        array2 = from_list(x2)
        self.assertEqual(array1, reverse_arr(array2))

    def test_concat(self):
        l1 = [None, 1]
        l2 = [1, None]
        array1 = from_list(l1)
        array2 = from_list(l2)
        self.assertEqual(concat(array1, array2), from_list([None, 1, 1, None]))

    def test_append_and_getitem(self):
        array = Dynamic_array()
        temp_list = [1, 2, 3, 4, 5, 6]
        for i in temp_list:
            array = append(array, i)
        get_a = get_array(array)
        self.assertEqual(get_a, temp_list)
        temp1 = get_item(array, 2)
        self.assertEqual(temp1, temp_list[2])
        temp1 = get_item(array, 5)
        self.assertEqual(temp1, temp_list[5])

    def test_filter(self):
        x = [1, 4, 6, 7, 9, 12, 17]
        array = from_list(x)
        temp1 = filter(array, is_odd)
        self.assertEqual(str(temp1), "[1, 7, 9, 17]")

        x2 = ['test', None, '', 'str', ' ', 'END']
        array2 = from_list(x2)
        temp2 = filter(array2, is_not_empty)
        self.assertEqual(str(temp2), "['test', 'str', 'END']")

        x3 = [1, 2, 3, 2, 5, 2, 7, 2, 9]
        array3 = from_list(x3)
        temp3 = filter(array3, remove_value_2)
        self.assertEqual(str(temp3), "[1, 3, 5, 7, 9]")

        array4 = from_list([])
        for i in range(1, 101):
            array4 = append(array4, i)
        temp4 = filter(array4, is_sqr)
        self.assertEqual(str(temp4), "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]")

        x4 = [1, 2, 3, 4, 5]
        array5 = from_list(x4)
        self.assertEqual([2, 4], to_list(filter(array5, lambda e: e % 2 == 0)))

    def test_map(self):
        array = from_list([2, 3, 4, 5, 6, 7, 8, 9])
        temp = map(array, my_square)
        self.assertEqual(str(temp), "[4, 9, 16, 25, 36, 49, 64, 81]")

        temp2 = map(temp, my_sqr)
        self.assertEqual(str(temp2), str(array))

        array = Dynamic_array()
        self.assertEqual(to_list(map(array, str)), [])
        array = from_list([1, 2, 3])
        self.assertEqual(to_list(map(array, str)), ["1", "2", "3"])
        self.assertEqual(to_list(map(array, lambda x: x + 1)), [2, 3, 4])

    def test_reduce(self):
        array = from_list([1, 2, 3, 4, 5])
        result = reduce(array, my_add)
        self.assertEqual(str(result), "15")
        self.assertEqual(reduce(array, lambda st, e: st + e), 15)

        array = from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = reduce(array, my_add)
        self.assertEqual(str(result), "55")
        self.assertEqual(reduce(array, lambda st, e: st + e), 55)

    def test_empty(self):
        array = Dynamic_array()
        self.assertEqual(empty(array), True)
        array = append(array, 1)
        self.assertEqual(empty(array), False)
        array = remove_value(array, 1)
        self.assertTrue(empty(array))
        array = append(array, 2)
        self.assertFalse(empty(array))

    def test_iter(self):
        x = [1, 2, 3]
        array = from_list(x)
        tmp = []
        try:
            it = iter(array)
            while True:
                tmp.append(next(it))
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(array), tmp)
        it = iter(Dynamic_array())
        self.assertRaises(StopIteration, lambda: next(it))

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        self.assertEqual(to_list(from_list(a)), a)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = from_list(lst)
        empty = Dynamic_array()
        self.assertEqual(concat(empty, a), a)
        self.assertEqual(concat(a, empty), a)

    @given(x1=st.lists(st.integers()),
           x2=st.lists(st.integers()),
           x3=st.lists(st.integers()))
    def test_monoid_associativity(self, x1, x2, x3):
        a = from_list(x1)
        b = from_list(x2)
        c = from_list(x3)

        # mconcar: (a*b)*c = a*(b*c)
        self.assertEqual(concat(a, concat(b, c)),
                         concat(concat(a, b), c))


# functions to test filter
def is_odd(x):
    return x % 2 == 1


# Delete None or empty string
def is_not_empty(s):
    if s is not None:
        return (len(s.strip()) > 0)
    return s is not None


# Filter out the number whose square root is an integer in 1 ~ 100
def is_sqr(x):
    return math.sqrt(x) % 1 == 0


def remove_value_2(x):
    return x != 2


# These are functions to test map
def my_square(n):
    return n * n


def my_sqr(x):
    return int(math.sqrt(x))


# Test of function of reduce
def my_add(x, y):
    return x+y


if __name__ == '__main__':
    unittest.main()
