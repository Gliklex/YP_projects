import tasks_regular
import pytest
"""Возвращает True, если год находится в интервале от 1800 до 2200."""

year_list = [(1800, True), (1999.1, False), (1999, True), (2200, True), ("2800", False)]


@pytest.mark.parametrize("year, result", year_list)
def test_match_13(year, result):
    assert tasks_regular.match_13(year) == result
