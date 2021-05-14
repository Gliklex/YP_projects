import my_queue_collection as mqc
import pytest

qc = mqc.QueueCollection()
list_adds_queue = [mqc.Queue([1, 3, 4]), mqc.Queue([1, 8, 4]), mqc.Queue([1, 5, 4, 1]), mqc.Queue([1, 1, 8, 4])]
for q in list_adds_queue:
    qc.add(q)

list_gets = [(qc[0:2], "[[1, 3, 4] - очередь, [1, 8, 4] - очередь]"),
             (qc[0], "[1, 3, 4] - очередь"),
             (qc[0:3], "[[1, 3, 4] - очередь, [1, 8, 4] - очередь, [1, 5, 4, 1] - очередь]")]


@pytest.mark.parametrize("qc_slice, expected_result", list_gets)
def test_qc__getitem__(qc_slice, expected_result):
    assert qc_slice.__str__() == expected_result
    assert qc_slice.__str__() == expected_result
    assert qc_slice.__str__() == expected_result
