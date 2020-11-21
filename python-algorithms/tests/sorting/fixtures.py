import pytest

@pytest.fixture
def raw_arr():
    yield [19, 17, 10, 1, 11, 18, 4, 0, 9, 3, 12, 14, 13, 2, 16, 5, 6, 7, 8, 15]

@pytest.fixture
def sorted_arr():
    yield list(range(20))