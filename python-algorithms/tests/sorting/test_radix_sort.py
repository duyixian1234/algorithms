from algorithms.sorting.radix_sort import radix_sort
from tests.sorting.fixtures import raw_arr, sorted_arr


def test_radix_sort(raw_arr, sorted_arr):
    arr = raw_arr.copy()
    assert radix_sort(arr) == sorted_arr