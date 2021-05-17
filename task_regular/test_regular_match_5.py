import tasks_regular
import pytest
"""Находит строку 2+3, не захватив остальные.
   Возвращает лист найденных значений, а на вход принимает строку."""
string_list = [('2+3 223 2223', ['2+3']),
               ('2+3 2+23 2+2+23 2+3', ['2+3', '2+3']),
               ('223 2223', [])]


@pytest.mark.parametrize("string, result", string_list)
def test_match_5(string, result):
    assert tasks_regular.match_5(string) == result