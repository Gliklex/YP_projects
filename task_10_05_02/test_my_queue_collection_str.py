import my_queue_collection as mqc
import pytest


def test__str__():
    art = mqc.QueueCollection()
    art.add(mqc.Queue([1, 2, 3]))
    assert art.__str__() == "![[1, 2, 3]]!"
