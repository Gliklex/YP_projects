import my_queue_collection as mqc
import pytest

list_inits = [(None, "![]!"), ([mqc.Queue([1, 2, 3])], "![[1, 2, 3] - очередь]!"),
              ([mqc.Queue([1, 2, 3]), mqc.Queue([1, 3, 3])], "![[1, 2, 3] - очередь, [1, 3, 3] - очередь]!")]


@pytest.mark.parametrize("add_q, expected_result", list_inits)
def test__init__(add_q, expected_result):
    assert mqc.QueueCollection(add_q).__str__() == expected_result

