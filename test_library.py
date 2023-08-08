import unittest
import library


def test_generate_random_number():
    random_number = library.generating_random_number()
    assert 0 <= random_number <= 1000


def test_generate_random_number_type():
    random_number = library.generating_random_number()
    assert isinstance(random_number, int)
