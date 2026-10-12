"""Відкриті тести задачі 3: рейтинг атрибутів якості.

Запуск: pytest tests/test_variant_03.py
Тут лише приклади з опису задачі; повний набір перевірок є у викладача.
"""
import pytest
from conftest import load

POWER = {"Клієнт": 3, "Директор": 4}
CONCERNS = [
    {"stakeholder": "Клієнт", "attribute": "продуктивність", "priority": 3},
    {"stakeholder": "Клієнт", "attribute": "зручність", "priority": 1},
    {"stakeholder": "Директор", "attribute": "вартість", "priority": 3},
    {"stakeholder": "Директор", "attribute": "продуктивність", "priority": 1},
]


def test_weights_and_ranks():
    result = load(3).rank_attributes(POWER, CONCERNS)
    assert [(r["attribute"], r["weight"], r["rank"]) for r in result] == [
        ("продуктивність", 13, 1), ("вартість", 12, 2), ("зручність", 3, 3)]


def test_share_and_key():
    result = load(3).rank_attributes(POWER, CONCERNS)
    assert [r["share"] for r in result] == [46.4, 42.9, 10.7]
    assert [r["key"] for r in result] == [True, True, False]


def test_unknown_stakeholder():
    with pytest.raises(ValueError) as info:
        load(3).rank_attributes(POWER, [{"stakeholder": "Хтось", "attribute": "безпека", "priority": 2}])
    assert str(info.value) == "Невідома сторона: Хтось"
