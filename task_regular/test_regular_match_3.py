import tasks_regular
import pytest
"""Находит строки по шаблону:
   буква 'a', буква 'b' любое количество раз, буква 'a'.
   Возвращает лист найденных значений, а на вход принимает строку"""

string_list = [('aa aba abba abbba abca abea', ['aba', 'abba', 'abbba']),
               ('aa aba abba abbbbbba abbba abca abea', ['aba', 'abba', 'abbbbbba', 'abbba']),
               ('aa aza arba arbba arbca abea', []),
               ('', [])]


@pytest.mark.parametrize("string, result", string_list)
def test_match_3(string, result):
    assert tasks_regular.match_3(string) == result