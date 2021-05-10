from queue import *
import pytest

element_list = [(1, "[1] - очередь"), (123, "[123] - очередь"), ([1, 2, 3], "[[1, 2, 3]] - очередь")]



@pytest.mark.parametrize("ele, expected", element_list)
def test_enqueue_pos(ele, expected):
    que = Queue([])
    que.enqueue(ele)
    assert que.__str__() == expected


def test_enqueue_neg():
    que = Queue([])
    with pytest.raises(ValueError):
        que.enqueue(Queue([1]))
