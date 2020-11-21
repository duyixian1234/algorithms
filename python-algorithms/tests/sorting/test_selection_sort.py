from algorithms.sorting.selection_sort import selection_sort
from tests.sorting.fixtures import raw_arr, sorted_arr


def test_selection_sort(raw_arr, sorted_arr):
    arr = raw_arr.copy()
    selection_sort(arr)
    assert arr == sorted_arr