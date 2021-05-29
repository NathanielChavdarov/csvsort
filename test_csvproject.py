import os

import pytest

import csvproject as cs


def test_pytestworking():
    assert 1 == 1


def test_csvsort():
    inputdata = [
        ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [6, 5, 7, 4, 8, 3, 9, 1, 2],
        [3, 4, 7, 6, 5, 9, 1, 7, 3],
        [3, 6, 5, 8, 9, 6, 5, 1, 9],
    ]
    expected = [
        ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [3, 6, 5, 8, 9, 6, 5, 1, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [6, 5, 7, 4, 8, 3, 9, 1, 2],
        [3, 4, 7, 6, 5, 9, 1, 7, 3],
    ]
    got = cs.sortdata(inputdata, "C")
    assert got == expected


def test_empty():
    with pytest.raises(ValueError):
        cs.sortdata([], 0)
