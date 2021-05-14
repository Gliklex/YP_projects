import my_queue_collection as mqc
import pytest


def test__str__():
    assert mqc.QueueCollection([mqc.Queue([1, 2, 3])]).__str__() == "![[1, 2, 3] - очередь]!"
