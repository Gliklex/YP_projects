import tasks_regular
import pytest
r"""Находит содержимое всех конструкций /...\ 
Возвращает лист найденных значений, а на вход принимает строку."""

string_list = [(r"bbb /aaa\ bbb /ccc\"", ['aaa', 'ccc']),
               (r"/b2a1b1ab2\ /aaa\ bbb /ccc\"", ['b2a1b1ab2', 'aaa', 'ccc']),
               (r"bbb aaa bbb ccc", [])]


@pytest.mark.parametrize("string, result", string_list)
def test_match_12(string, result):
    assert tasks_regular.match_12(string) == result