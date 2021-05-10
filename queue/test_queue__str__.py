from queue import *
import pytest

que_list = [(Queue([]), "[] - пустая очередь"), (Queue([1, 2, 3]), "[1, 2, 3] - очередь")]


@pytest.mark.parametrize("que, expected_str", que_list)
def test__str__(que, expected_str):
    assert Queue.__str__(que) == expected_str


value_list = [(1, TypeError), ("123", TypeError)]


@pytest.mark.parametrize("val, expected_raise", value_list)
def test__str___neg(val, expected_raise):
    with pytest.raises(expected_raise):
        Queue(val)
