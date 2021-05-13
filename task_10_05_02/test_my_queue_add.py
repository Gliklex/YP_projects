import my_queue_collection as mqc
import pytest


list_adds = [(mqc.Queue([1, 3, 4]), [[1, 3, 4]])]


@pytest.mark.parametrize("q_value, expected_result", list_adds)
def test_mqc_add(q_value, expected_result):
    q = mqc.QueueCollection()
    q.add(q_value)
    assert q.list_queue == expected_result
