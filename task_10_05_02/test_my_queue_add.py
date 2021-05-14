import my_queue_collection as mqc
import pytest


list_adds = [(mqc.Queue([1, 3, 4]), "![[1, 3, 4] - очередь]!"), (mqc.Queue([]), "![[] - пустая очередь]!")]


@pytest.mark.parametrize("q_value, expected_result", list_adds)
def test_mqc_add(q_value, expected_result):
    qc = mqc.QueueCollection()
    qc.add(q_value)
    assert qc.__str__() == expected_result
