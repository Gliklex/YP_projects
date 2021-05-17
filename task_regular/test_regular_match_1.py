import tasks_regular
import pytest

string_list = [("ahb acb aeb aeeb adcb axeb", ["ahb", "acb", "aeb"]),
               ("aeeb adcb axeb ahb acb arb aeb aeeb adcb axeb", ["ahb", "acb", "arb", "aeb"]),
               ("aeeb adcb axeb", [])]


@pytest.mark.parametrize("string, result", string_list)
def test_match_1(string, result):
    assert tasks_regular.match_1(string) == result


