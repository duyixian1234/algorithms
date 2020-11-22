from algorithms.sorting.merge_sort import merge_sort, inplace_merge_sort
from tests.sorting.fixtures import raw_arr, sorted_arr


def test_merge_sort(raw_arr, sorted_arr):
    arr = raw_arr.copy()
    merge_sort(arr)
    assert arr == sorted_arr


def test_inplace_merge_sort(raw_arr, sorted_arr):
    arr = raw_arr.copy()
    inplace_merge_sort(arr)
    assert arr == sorted_arr