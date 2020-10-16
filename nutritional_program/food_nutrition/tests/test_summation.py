from django.test import TestCase
from .summation import summation
import pytest


@pytest.mark.parametrize(
    "test_x, test_y, expected",
    [
        (3, 5, 8),
        (2, 4, 6),
    ],
)
def test_summation(test_x, test_y, expected):
    assert summation(test_x, test_y) == expected
