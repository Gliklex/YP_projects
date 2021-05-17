import re


def match_1(string):
    """Находит строки по шаблону: буква 'a', любой символ, буква 'b'
       возвращает лист найденных значений, а на вход принимает строку."""
    pattern = r"a.b"
    if isinstance(string, str):
        return re.findall(pattern, string)

    else:
        raise TypeError("Неверный тип аргумента")


def match_2(string):
    """Находит строки abba adca abea по шаблону:
       буква 'a', 2 любых символа, буква 'a'.
       Возвращает лист найденных значений, а на вход принимает строку."""
    pattern = r"a..a"
    if isinstance(string, str):
        return re.findall(pattern, string)
    else:
        raise TypeError("Неверный тип аргумента")


def match_3(string):
    """Находит строки aba, abba, abbba по шаблону:
       буква 'a', буква 'b' любое количество раз, буква 'a'.
       Возвращает лист найденных значений, а на вход принимает строку"""
    pattern = r"ab+a"
    if isinstance(string, str):
        return re.findall(pattern, string)
    else:
        raise TypeError("Неверный тип аргумента")


def match_4(string):#!
    """Находит строки по шаблону:
       строка 'ab' повторяется 1 или более раз
       Возвращает лист найденных значений, а на вход принимает строку."""
    pattern = r"(?:ab)+"
    if isinstance(string, str):
        return re.findall(pattern, string)
    else:
        raise TypeError("Неверный тип аргумента")


def match_5(string):
    """Находит строку 2+3, не захватив остальные.
       Возвращает лист найденных значений, а на вход принимает строку."""
    pattern = r"2\+3"
    if isinstance(string, str):
        return re.findall(pattern, string)
    else:
        raise TypeError("Неверный тип аргумента")


def match_6(string):
    """Находит строки 2+3, 2++3, 2+++3, не захватив остальные (+ может быть любое количество).
        Возвращает лист найденных значений, а на вход принимает строку."""
    pattern = r"2\++3"
    if isinstance(string, str):
        return re.findall(pattern, string)
    else:
        raise TypeError("Неверный тип аргумента")


def match_7(string):
    """Находит строки вида aba, в которых 'b' встречается менее 3-х раз (включительно).
        Возвращает лист найденных значений, а на вход принимает строку."""
    pattern = r"ab{1,3}a"
    if isinstance(string, str):
        return re.findall(pattern, string)
    else:
        raise TypeError("Неверный тип аргумента")


def match_8(string):
    """Находит строки следующего вида: по краям стоят буквы 'a' и 'b', а между ними - не число.
       Возвращает лист найденных значений, а на вход принимает строку."""
    pattern = r"a\Db"
    if isinstance(string, str):
        return re.findall(pattern, string)
    else:
        raise TypeError("Неверный тип аргумента")


def match_9(string):
    """Находит строки следующего вида: по краям стоят буквы 'a', а между ними - не 'e' и не 'x'.
       Возвращает лист найденных значений, а на вход принимает строку."""
    pattern = r"a[^ex]a"
    if isinstance(string, str):
        return re.findall(pattern, string)
    else:
        raise TypeError("Неверный тип аргумента")


def match_10(string):
    """Находит все слова по шаблону:
    любая кириллическая буква любое количество раз.
    Возвращает лист найденных значений, а на вход принимает строку."""
    pattern = r"[а-яё]+"
    if isinstance(string, str):
        return re.findall(pattern, string, flags=re.I)
    else:
        raise TypeError("Неверный тип аргумента")


def match_11(string):
    """Находит строки следующего вида:
    по краям стоят буквы 'a',
    а между ними - или буква 'e' любое количество раз
    или по краям стоят буквы 'a', а между ними - буква 'x' любое количество раз.
    Возвращает лист найденных значений, а на вход принимает строку."""
    pattern = r"ae+a|ax+a"
    if isinstance(string, str):
        return re.findall(pattern, string)
    else:
        raise TypeError("Неверный тип аргумента")


def match_12(string):   #!
    """Находит содержимое всех конструкций /...\\
    Возвращает лист найденных значений, а на вход принимает строку."""
    pattern = r'/(.+?)\\'
    if isinstance(string, str):
        return re.findall(pattern, string)
    else:
        raise TypeError("Неверный тип аргумента")


def match_13(year):
    """Возвращает True, если год находится в интервале от 1800 до 2200."""
    year = str(year)
    pattern = r"1[8-9][0-9][0-9]|2[0-1][0-9][0-9]|2200"
    res_list = re.findall(pattern, year)
    if year in res_list:
        return True
    else:
        return False


def match_14(string):
    """Возвращает True,
     если переданная строка является корректным временем вида '9.59 am', '12.30 pm'."""
    pattern = \
        r"1[0-1]\.[0-5][0-9]\sam|[0-9]\.[0-5][0-9]\sam|[1-2][2-3|0]\.[0-5][0-9]\spm|1[2-9]\.[0-5][0-9]\spm|24\.00 pm"
    if isinstance(string, str):
        res_list = re.findall(pattern, string)
        if string in res_list:
            return True
        else:
            return False
    else:
        raise TypeError("Неверный тип аргумента")


