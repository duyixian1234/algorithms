from typing import List, TypeVar

DataT = TypeVar("DataT")


def selection_sort(arr: List[DataT]):
    length = len(arr)
    for i in range(length):
        smallest = arr[i]
        for j in range(i + 1, length):
            if arr[smallest] > arr[j]:
                smallest = j
        arr[smallest], arr[i] = arr[i], arr[smallest]
