import tasks_regular
import pytest
"""Находит строки следующего вида: по краям стоят буквы 'a', а между ними - не 'e' и не 'x'.
   Возвращает лист найденных значений, а на вход принимает строку."""

string_list = [('aba aea aca aza axa a-a a#a', ['aba', 'a a', 'a a', 'a a', 'a a', 'a a']),
               ('aba aca aza a-a a#a', ['aba', 'aca', 'aza', 'a-a', 'a#a']),
               ('abra raxa saea eaxa xaxa', [])]



@pytest.mark.parametrize("string, result", string_list)
def test_match_9(string, result):
    assert tasks_regular.match_9(string) == result