import tasks_regular
import pytest
"""Находит все слова по шаблону:
любая кириллическая буква любое количество раз.
Возвращает лист найденных значений, а на вход принимает строку."""

string_list = [('ааа ббб ёёё ззз ййй ААА БББ ЁЁЁ ЗЗЗ ЙЙЙ',
                ['ааа', 'ббб', 'ёёё', 'ззз', 'ййй', 'ААА', 'БББ', 'ЁЁЁ', 'ЗЗЗ', 'ЙЙЙ']),
               ('ааа bbb ёёё zzz ййй AAAa БББ ЁЁЁ ЗЗЗ ЙЙЙ аАаА',
                ['ааа', 'ёёё', 'ййй', 'БББ', 'ЁЁЁ', 'ЗЗЗ', 'ЙЙЙ', 'аАаА']),
               ('AAA bbb ccc ggg GGG TTT', [])]


@pytest.mark.parametrize("string, result", string_list)
def test_match_10(string, result):
    assert tasks_regular.match_10(string) == result