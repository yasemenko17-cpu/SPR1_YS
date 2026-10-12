"""Відкриті тести задачі 4: перевірка сценарію якості.

Запуск: pytest tests/test_variant_04.py
Тут лише приклади з опису задачі; повний набір перевірок є у викладача.
"""
import pytest
from conftest import load

BASE = dict(attribute="продуктивність", source="студент", stimulus="відкриває каталог", environment="300 користувачів",
            artifact="вебзастосунок", response="показує список", measure="p95 не більше 800 мс")

CASES = [
    ({}, []),
    ({"measure": "відповідь швидко"}, ["міра:немає_числа_з_одиницею", "розмите:швидко"]),
    ({"source": " "}, ["порожнє:source"]),
    ({"measure": "не більше 2 с"}, ["міра:немає_процентиля"]),
    ({"attribute": "доступність", "measure": "101 %"}, ["міра:понад_100%"]),
    ({"attribute": "краса"}, ["атрибут:невідомий"]),
]


@pytest.mark.parametrize("change,expected", CASES, ids=[f"T04-{i}" for i in range(len(CASES))])
def test_check_scenario(change, expected):
    assert load(4).check_scenario({**BASE, **change}) == expected
