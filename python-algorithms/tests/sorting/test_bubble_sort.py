from algorithms.sorting.bubble_sort import bubble_sort
from tests.sorting.fixtures import raw_arr, sorted_arr


def test_bubble_sort(raw_arr, sorted_arr):
    arr = raw_arr.copy()
    bubble_sort(arr)
    assert arr == sorted_arr