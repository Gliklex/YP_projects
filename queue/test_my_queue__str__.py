from my_queue import *
import pytest

que_list = [(Queue([]), "[] - пустая очередь"), (Queue([1, 2, 3]), "[1, 2, 3] - очередь")]


@pytest.mark.parametrize("que, expected_str", que_list)
def test__str__(que, expected_str):
    assert Queue.__str__(que) == expected_str





