import my_queue_collection as mqc
import pytest


def test__init__():
    assert mqc.QueueCollection().list_queue == []

