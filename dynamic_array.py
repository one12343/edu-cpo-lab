import ctypes
import operator

class Dynamic_array:

    def __init__(self,capacity=10):
        'Create an empty array.'
        self._n = 0  # size
        self._capacity = capacity
        self._A = make_array(self,self._capacity)

    def __str__(self):
        return str(get_array(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                # self._n == other._n and
                # self._capacity == other._capacity and
                operator.eq(get_array(self),get_array(other))
                )
    def __getitem__(self, index):
        return get_array(self)[index]

    def __setitem__(self, index, newItem):
        self._A[index] = newItem

def get_len(Dynamic_array):
    return Dynamic_array._n

def is_empty(Dynamic_array):
    return Dynamic_array._n == 0

def get_item(Dynamic_array, k):
    if not 0 <= k < Dynamic_array._n:
        raise ValueError('invalid index')
    return Dynamic_array._A[k]

def make_array(Dynamic_array, c):
    return (c * ctypes.py_object)()

def array_resize(Dynamic_array, c):
    B = make_array(Dynamic_array,c)
    # After expansion, you need to copy the elements in the original array to the new array
    for k in range(Dynamic_array._n):
        B[k] = Dynamic_array._A[k]
    Dynamic_array._A = B
    Dynamic_array._capacity = c
    return Dynamic_array

def append(Dynamic_array0, obj):
    Dynamic_array = new_item(Dynamic_array0)
    # When the current element of the array is full, the expansion capacity is twice that of the original one, and it is added
    if Dynamic_array._n == Dynamic_array._capacity:
        Dynamic_array=array_resize(Dynamic_array,2 * Dynamic_array._capacity)
    Dynamic_array._A[Dynamic_array._n] = obj
    Dynamic_array._n += 1
    return Dynamic_array

def remove_value(Dynamic_array0, value):
    Dynamic_array = new_item(Dynamic_array0)
    for k in range(Dynamic_array._n):
        if Dynamic_array._A[k] == value:
            for j in range(k, Dynamic_array._n - 1):
                Dynamic_array._A[j] = Dynamic_array._A[j + 1]
            Dynamic_array._A[Dynamic_array._n - 1] = None
            Dynamic_array._n -= 1
            return Dynamic_array
    raise ValueError('value not found')

def remove_index(Dynamic_array0, index):
    Dynamic_array = new_item(Dynamic_array0)
    if index>=Dynamic_array0._n:
        ValueError('index out of line')

    for k in range(Dynamic_array._n):
        if k == index:
            for j in range(k, Dynamic_array._n - 1):
                Dynamic_array._A[j] = Dynamic_array._A[j + 1]
            Dynamic_array._A[Dynamic_array._n - 1] = None
            Dynamic_array._n -= 1
            return Dynamic_array

def member(value,Dynamic_array):
    if Dynamic_array==None:
        arr_len=0
    else: arr_len=Dynamic_array._n
    for k in range(arr_len):
        if Dynamic_array._A[k] == value:
            return True
    return False

def print_all(Dynamic_array):
    for i in range(Dynamic_array._n):
        print(Dynamic_array._A[i], end=' ')
    print()

def get_array(Dynamic_array):
    temp_list=[]
    for i in range(Dynamic_array._n):
        temp_list.append(Dynamic_array._A[i])
    return temp_list

def cons(a,Dynamic_array1):
    Dynamic_array0 = new_item(Dynamic_array1)

    if type(a)!=list:
        if Dynamic_array0._n == Dynamic_array0._capacity:
            Dynamic_array0=array_resize(Dynamic_array0,2 * Dynamic_array0._capacity)

        for i in range(Dynamic_array0._n-1,-1,-1):
            Dynamic_array0._A[i+1]=Dynamic_array0._A[i]

        Dynamic_array0._n += 1
        Dynamic_array0._A[0]=a
    elif type(a)==list:
        if Dynamic_array0._n+len(a)>Dynamic_array0._capacity:
            Dynamic_array0=array_resize(Dynamic_array0,2 * Dynamic_array0._capacity)

        new_empty=Dynamic_array()
        for i in a:
            new_empty=append(new_empty,i)
        for i in range(Dynamic_array0._n):
            new_empty=append(new_empty,Dynamic_array0._A[i])
        Dynamic_array0=new_empty
    return Dynamic_array0

def new_item(Dynamic_array0):
    new_Dynamic_array=Dynamic_array(Dynamic_array0._capacity)
    new_Dynamic_array._n=Dynamic_array0._n
    new_Dynamic_array._capacity=Dynamic_array0._capacity
    for i in range(Dynamic_array0._n):
        new_Dynamic_array._A[i]=Dynamic_array0._A[i]
    return new_Dynamic_array

def reverse_arr(Dynamic_array1):
    Dynamic_array0 = new_item(Dynamic_array1)
    temp_list=[]
    for i in range(Dynamic_array0._n):
        temp_list.append(Dynamic_array0._A[i])
    temp_list.reverse()
    for i in range(Dynamic_array0._n):
        Dynamic_array0._A[i] = temp_list[i]
    return Dynamic_array0

def to_list(Dynamic_array):
    return get_array(Dynamic_array)

def from_list(temp_list):
    Dynamic_array0 = Dynamic_array()
    while(Dynamic_array0._capacity<len(temp_list)):
        Dynamic_array0=array_resize(Dynamic_array0,2 * Dynamic_array0._capacity)
    Dynamic_array0._n=len(temp_list)
    for i in range(Dynamic_array0._n):
        Dynamic_array0._A[i]=temp_list[i]
    return Dynamic_array0

def concat(Dynamic_array1,Dynamic_array2):
    temp_list=get_array(Dynamic_array1)
    return cons(temp_list,Dynamic_array2)

def filter(Dynamic_array1,new_function):
    Dynamic_array0 = new_item(Dynamic_array1)
    temp_list=[]
    for i in range(Dynamic_array0._n):
        flag=new_function(Dynamic_array0._A[i])

        if flag==False:
            temp_list.append(Dynamic_array0._A[i])
    for i in temp_list:
        Dynamic_array0=remove_value(Dynamic_array0,i)
    return Dynamic_array0

def map(Dynamic_array1,new_function):
    Dynamic_array0 = new_item(Dynamic_array1)
    for i in range(Dynamic_array0._n):
        Dynamic_array0._A[i] = new_function(Dynamic_array0._A[i])
    return Dynamic_array0

def reduce(Dynamic_array1,new_function):
    Dynamic_array0 = new_item(Dynamic_array1)
    temp=Dynamic_array0._A[0]
    result=0
    for i in range(1,Dynamic_array0._n):
        result = new_function(temp,Dynamic_array0._A[i])
        temp=result
    return result

def empty(Dynamic_array):
    return Dynamic_array._n==0
