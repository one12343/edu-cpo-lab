import ctypes
import operator


class Dynamic_array:

    def __init__(self, capacity=10):
        # Create an empty array.
        self._n = 0  # size
        self._capacity = capacity
        self._A = make_array(self, self._capacity)

    def __str__(self):
        return str(get_array(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                operator.eq(get_array(self), get_array(other))
                )

    def __getitem__(self, index):
        return get_array(self)[index]

    def __setitem__(self, index, newItem):
        self._A[index] = newItem

    def __copy__(self):
        return self


def get_len(dynamic_array):
    return dynamic_array._n


def is_empty(dynamic_array):
    return dynamic_array._n == 0


def get_item(dynamic_array, k):
    if not 0 <= k < dynamic_array._n:
        raise ValueError('invalid index')
    return dynamic_array._A[k]


def make_array(dynamic_array, c):
    return (c * ctypes.py_object)()


def array_resize(dynamic_array, c):
    B = make_array(dynamic_array, c)
    for k in range(dynamic_array._n):
        B[k] = dynamic_array._A[k]
    dynamic_array._A = B
    dynamic_array._capacity = c
    return dynamic_array


def append(dynamic_array, obj):
    if dynamic_array._n == dynamic_array._capacity:
        dynamic_array = array_resize(dynamic_array,
                                     2 * dynamic_array._capacity)
    dynamic_array._A[dynamic_array._n] = obj
    dynamic_array._n += 1
    return dynamic_array


def remove_value(dynamic_array1, value):
    dynamic_array = new_item(dynamic_array1)
    for k in range(dynamic_array._n):
        if dynamic_array._A[k] == value:
            for j in range(k, dynamic_array._n - 1):
                dynamic_array._A[j] = dynamic_array._A[j + 1]
            dynamic_array._A[dynamic_array._n - 1] = None
            dynamic_array._n -= 1
            return dynamic_array
    raise ValueError('value not found')


def remove_index(dynamic_array1, index):
    dynamic_array = new_item(dynamic_array1)
    if index >= dynamic_array._n:
        ValueError('index out of line')

    for k in range(dynamic_array._n):
        if k == index:
            for j in range(k, dynamic_array._n - 1):
                dynamic_array._A[j] = dynamic_array._A[j + 1]
            dynamic_array._A[dynamic_array._n - 1] = None
            dynamic_array._n -= 1
            return dynamic_array


def member(value, dynamic_array):
    if dynamic_array is None:
        arr_len = 0
    else:
        arr_len = dynamic_array._n
    for k in range(arr_len):
        if dynamic_array._A[k] == value:
            return True
    return False


def print_all(dynamic_array):
    for i in range(dynamic_array._n):
        print(dynamic_array._A[i])


def get_array(dynamic_array):
    temp_list = []
    for i in range(dynamic_array._n):
        temp_list.append(dynamic_array._A[i])
    return temp_list


def cons(a, dynamic_array0):
    dynamic_array = new_item(dynamic_array0)
    if type(a) != list:
        if dynamic_array._n == dynamic_array._capacity:
            dynamic_array = array_resize(dynamic_array,
                                         2 * dynamic_array._capacity)

        for i in range(dynamic_array._n-1, -1, -1):
            dynamic_array._A[i+1] = dynamic_array._A[i]

        dynamic_array._n += 1
        dynamic_array._A[0] = a
    elif type(a) == list:
        if dynamic_array._n+len(a) > dynamic_array._capacity:
            dynamic_array = array_resize(dynamic_array,
                                         2 * dynamic_array._capacity)

        new_empty = Dynamic_array()
        for i in a:
            new_empty = append(new_empty, i)
        for i in range(dynamic_array._n):
            new_empty = append(new_empty, dynamic_array._A[i])
        dynamic_array = new_empty
    return dynamic_array


def new_item(dynamic_array):
    new_dynamic_array = Dynamic_array(dynamic_array._capacity)
    new_dynamic_array._n = dynamic_array._n
    new_dynamic_array._capacity = dynamic_array._capacity
    for i in range(dynamic_array._n):
        new_dynamic_array._A[i] = dynamic_array._A[i]
    return new_dynamic_array


def reverse_arr(dynamic_array1):
    dynamic_array=new_item(dynamic_array1)
    temp_list = []
    for i in range(dynamic_array._n):
        temp_list.append(dynamic_array._A[i])
    temp_list.reverse()
    for i in range(dynamic_array._n):
        dynamic_array._A[i] = temp_list[i]
    return dynamic_array


def to_list(dynamic_array):
    return get_array(dynamic_array)


def from_list(temp_list):
    dynamic_array = Dynamic_array()
    while(dynamic_array._capacity < len(temp_list)):
        dynamic_array = array_resize(dynamic_array,
                                     2 * dynamic_array._capacity)
    dynamic_array._n = len(temp_list)
    for i in range(dynamic_array._n):
        dynamic_array._A[i] = temp_list[i]
    return dynamic_array


def concat(dynamic_array1, dynamic_array2):
    temp_list = get_array(dynamic_array1)
    return cons(temp_list, dynamic_array2)


def filter(dynamic_array1, new_function):
    dynamic_array = new_item(dynamic_array1)
    temp_list = []
    for i in range(dynamic_array._n):
        flag = new_function(dynamic_array._A[i])

        if flag is False:
            temp_list.append(dynamic_array._A[i])
    for i in temp_list:
        dynamic_array = remove_value(dynamic_array, i)
    return dynamic_array


def map(dynamic_array1, new_function):
    dynamic_array = new_item(dynamic_array1)
    for i in range(dynamic_array._n):
        dynamic_array._A[i] = new_function(dynamic_array._A[i])
    return dynamic_array


def reduce(dynamic_array1, new_function):
    dynamic_array = new_item(dynamic_array1)
    temp = dynamic_array._A[0]
    result = 0
    for i in range(1, dynamic_array._n):
        result = new_function(temp, dynamic_array._A[i])
        temp = result
    return result


def empty(dynamic_array):
    return dynamic_array._n == 0
