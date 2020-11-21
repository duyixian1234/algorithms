from algorithms.sorting.quick_sort import quick_sort
from tests.sorting.fixtures import raw_arr, sorted_arr


def test_quick_sort(raw_arr, sorted_arr):
    arr = raw_arr.copy()
    quick_sort(arr)
    assert arr == sorted_arr