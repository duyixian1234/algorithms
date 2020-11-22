from typing import List
import math


def radix_sort(arr: List[int]):
    max_base = get_max_base(arr)
    base = 1
    buckets = [arr]
    while base <= max_base:
        buckets = _radix_sort(buckets, base)
        base *= 10
    # At last run,negative numbers will br put in bucket 9, beacuse a negative number `//` a positive number returns -1 and -1 mod 10 returns 9
    return buckets[9] + buckets[0]


def get_max_base(arr: List[int]):
    return 10 ** (int(math.log10(max(abs(num) for num in arr))) + 1)


def _radix_sort(buckets: List[List[int]], base: int):
    new = [[] for _ in range(10)]
    for num in gen_nums(buckets):
        bit = num // base % 10
        new[bit].append(num)
    return new


def gen_nums(buckets: List[List[int]]):
    for bucket in buckets:
        for num in bucket:
            yield num
