from queue import *
import pytest

q = Queue([11, 12])
list_val = [(Queue([]), []), (Queue([1, 2, 3]), [1, 2, 3]), (Queue(q), [11, 12])]


@pytest.mark.parametrize("que, expected_val", list_val)
def test__init__pos(que, expected_val):
    assert que.list_elements == expected_val


value_list = [(1, TypeError), ("123", TypeError)]


@pytest.mark.parametrize("val, expected_raise", value_list)
def test__init___neg(val, expected_raise):
    with pytest.raises(expected_raise):
        Queue(val)
