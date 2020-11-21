from typing import List, TypeVar

DataT = TypeVar("DataT")


def heap_sort(arr: List[DataT]):
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


def build_max_heap(arr: List[DataT]):
    length = len(arr)
    for i in range(length // 2, -1, -1):
        heapify(arr, i, length)


def heapify(arr: List[DataT], index, length):
    left, right = 2 * index, 2 * index + 1
    largest = index
    if left < length and arr[left] > arr[largest]:
        largest = left
    if right < length and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, largest, length)
