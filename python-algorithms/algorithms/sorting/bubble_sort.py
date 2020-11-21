from typing import List,TypeVar

DataT = TypeVar('DataT')

def bubble_sort(arr:List[DataT]):
    length = len(arr)
    for i in range(length):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1], arr[j]
