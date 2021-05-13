import my_queue_collection as mqc
import pytest


list_adds = [(mqc.Queue([1, 3, 4]), mqc.Queue([1, 8, 4]), 1, [[1, 3, 4]])]


@pytest.mark.parametrize("q_value, q_value2, remove_value, expected_result", list_adds)
def test_mqc_remove(q_value, q_value2, remove_value, expected_result):
    qc = mqc.QueueCollection()
    qc.add(q_value)
    qc.add(q_value2)
    qc.remove(remove_value)
    assert qc.list_queue == expected_result
