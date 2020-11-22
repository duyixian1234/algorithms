from typing import List, TypeVar

DataT = TypeVar("DataT")


def inplace_merge_sort(arr: List[DataT]):
    length = len(arr)
    _inplace_merge_sort(arr, 0, length - 1)


def _inplace_merge_sort(arr: List[DataT], low: int, high: int):
    if low < high:
        mid = (low + high) // 2
        _inplace_merge_sort(arr, low, mid)
        _inplace_merge_sort(arr, mid + 1, high)
        inplace_merge(arr, low, mid, high)


def inplace_merge(arr: List[DataT], start: int, mid: int, end: int):
    start_2 = mid + 1
    if arr[mid] <= arr[start_2]:
        return

    while start <= mid and start_2 <= end:
        if arr[start] <= arr[start_2]:
            start += 1
        else:
            value = arr[start_2]
            for index in range(start_2, start - 1, -1):
                arr[index] = arr[index - 1]
            arr[start] = value
            start += 1
            mid += 1
            start_2 += 1


def merge_sort(arr: List[DataT]):
    length = len(arr)
    _merge_sort(arr, 0, length - 1)


def _merge_sort(arr: List[DataT], low: int, high: int):
    if low < high:
        mid = (low + high) // 2
        _merge_sort(arr, low, mid)
        _merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)


def merge(arr: List[DataT], low: int, mid: int, high: int):
    if arr[mid] <= arr[mid + 1]:
        return

    left = arr[low : mid + 1]
    right = arr[mid + 1 : high + 1]
    l_size = len(left)
    r_size = len(right)
    l = 0
    r = 0
    pos = low

    while l < l_size and r < r_size:
        if left[l] <= right[r]:
            arr[pos] = left[l]
            l += 1
        else:
            arr[pos] = right[r]
            r += 1
        pos += 1

    if l < l_size:
        arr[pos : high + 1] = left[l:]
    else:
        arr[pos : high + 1] = right[r:]
