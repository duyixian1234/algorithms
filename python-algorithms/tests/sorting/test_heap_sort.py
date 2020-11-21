from algorithms.sorting.heap_sort import heap_sort
from tests.sorting.fixtures import raw_arr, sorted_arr


def test_heap_sort(raw_arr, sorted_arr):
    arr = raw_arr.copy()
    heap_sort(arr)
    assert arr == sorted_arr