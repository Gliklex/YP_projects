from queue import *
import pytest

q = Queue([11, 12])
list_val = [(Queue([1]), []), (Queue([1, 2, 3]), [2, 3]), (Queue(q), [12])]


@pytest.mark.parametrize("que, expected_val", list_val)
def test_dequeue(que, expected_val):
    que.dequeue()
    assert que.list_elements == expected_val

