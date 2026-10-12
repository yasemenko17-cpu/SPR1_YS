"""Відкриті тести задачі 9: напруження між драйверами.

Запуск: pytest tests/test_variant_09.py
Тут лише приклади з опису задачі; повний набір перевірок є у викладача.
"""
from conftest import load


def test_single_tension():
    drivers = [{"id": "D1", "attribute": "безпека", "weight": 3}, {"id": "D2", "attribute": "зручність", "weight": 2}]
    assert load(9).find_tensions(drivers) == [
        {"a": "D1", "b": "D2", "pair": ["безпека", "зручність"], "strength": 3, "severity": 18, "winner": "D1"}]


def test_equal_weights_have_no_winner():
    drivers = [{"id": "D1", "attribute": "вартість", "weight": 2}, {"id": "D2", "attribute": "доступність", "weight": 2}]
    assert load(9).find_tensions(drivers)[0]["winner"] is None


def test_no_tension_for_same_attribute():
    drivers = [{"id": "D1", "attribute": "безпека", "weight": 3}, {"id": "D2", "attribute": "безпека", "weight": 1}]
    assert load(9).find_tensions(drivers) == []
