import tasks_regular
import pytest
"""Находит строки abba adca abea по шаблону:
   буква 'a', 2 любых символа, буква 'a'.
   Возвращает лист найденных значений, а на вход принимает строку."""

string_list = [('aba aca aea abba adca abea', ['abba', 'adca', 'abea']),
               ('aba aca absda ad!da aea abba adca abea', ['abba', 'adca', 'abea']),
               ('aba aca aea aba aca aea', []),
               ('abba', ['abba'])]


@pytest.mark.parametrize("string, result", string_list)
def test_match_2(string, result):
    assert tasks_regular.match_2(string) == result