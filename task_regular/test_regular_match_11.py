import tasks_regular
import pytest
"""Находит строки следующего вида:
по краям стоят буквы 'a',
а между ними - или буква 'e' любое количество раз
или по краям стоят буквы 'a', а между ними - буква 'x' любое количество раз.
Возвращает лист найденных значений, а на вход принимает строку."""

string_list = [('aeeea aeea aea axa axxa axxxa', ['aeeea', 'aeea', 'aea', 'axa', 'axxa', 'axxxa']),
               ('ae1eea ae1aea aea axa axxa axxxa', ['aea', 'aea', 'axa', 'axxa', 'axxxa']),
               ('arra ahha aba ada aaexa axsxsxsa', [])]


@pytest.mark.parametrize("string, result", string_list)
def test_match_11(string, result):
    assert tasks_regular.match_11(string) == result