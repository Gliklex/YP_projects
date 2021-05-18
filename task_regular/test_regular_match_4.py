import tasks_regular
import pytest
"""Находит строки по шаблону:
   строка 'ab' повторяется 1 или более раз
   Возвращает лист найденных значений, а на вход принимает строку."""

string_list = [('ab abab abab abababab abea', ['ab', 'abab', 'abab', 'abababab']),
               ('ab abab abab abababab abea ab ba', ['ab', 'abab', 'abab', 'abababab', 'ab']),
               ('eara orba barbrarba', [])]


@pytest.mark.parametrize("string, result", string_list)
def test_match_4(string, result):
    assert tasks_regular.match_4(string) == result