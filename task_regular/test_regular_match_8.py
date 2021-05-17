import tasks_regular
import pytest
"""Находит строки следующего вида: по краям стоят буквы 'a' и 'b', а между ними - не число.
   Возвращает лист найденных значений, а на вход принимает строку."""

string_list = [('avb a1b a2b a3b a4b a5b abb acb', ['avb', 'abb', 'acb']),
               ('avb a b a2b a3b a4b atb abb acb', ['avb', 'a b', 'atb', 'abb', 'acb']),
               ('a2b a1b a2b a3b a4b a1b a88b a9b', [])]


@pytest.mark.parametrize("string, result", string_list)
def test_match_8(string, result):
    assert tasks_regular.match_8(string) == result