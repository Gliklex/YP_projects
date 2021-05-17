import tasks_regular
import pytest
"""Находит строки вида aba, в которых 'b' встречается менее 3-х раз (включительно).
    Возвращает лист найденных значений, а на вход принимает строку."""

string_list = [('aa aba abba abbba abbbba abbbbba', ['aba', 'abba', 'abbba']),
               ('aa aba abba  abbbba abbbbba abbbbba abbbbba', ['aba', 'abba']),
               ('aa aaa aaaa  abbbba abbbbba abbbbba abbbbba', [])]


@pytest.mark.parametrize("string, result", string_list)
def test_match_7(string, result):
    assert tasks_regular.match_7(string) == result