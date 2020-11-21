from typing import List, TypeVar

DataT = TypeVar("DataT")


def quick_sort(arr: List[DataT]):
    _quick_sort(arr, 0, len(arr) - 1)


def _partion(arr: List[DataT], low: int, high: int):
    pivot = high
    i = low - 1
    j = high
    while True:
        i += 1
        while arr[i] < arr[pivot]:
            i += 1
        j -= 1
        while j and arr[j] > arr[pivot]:
            j -= 1
        if i >= j:
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return i


def _quick_sort(arr: List[DataT], low: int, high: int):
    if low >= high:
        return
    p = _partion(arr, low, high)
    _quick_sort(arr, low, p - 1)
    _quick_sort(arr, p + 1, high)
