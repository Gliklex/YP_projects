import tasks_regular
import pytest
"""Возвращает True,
 если переданная строка является корректным временем вида '9.59 am', '12.30 pm'."""

time_list = [('9.59 am', True), ('7.30 pm', True), ('11.30 am', True), ('13.30 am', False), ('12.30 pm', True),
             ('11.30 pm', True), ('11.тридцать', False), ('11.59 pm', True), ('1.11 am', True), ('', False),
             ('asdsad 9.59 am', False), ('9.59 am asdsad', False), ('asdsad 9.59 am asdsad', False)]


@pytest.mark.parametrize("string, result", time_list)
def test_match_14(string, result):
    assert tasks_regular.match_14(string) == result