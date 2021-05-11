from my_queue import *
import pytest

element_list = [(1, [1]), (123, [123]), ([1, 2, 3], [[1, 2, 3]])]


@pytest.mark.parametrize("ele, expected", element_list)
def test_enqueue_pos(ele, expected):
    que = Queue([])
    que.enqueue(ele)
    assert que.list_elements == expected

