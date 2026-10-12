"""Відкриті тести задачі 2: карта зацікавлених сторін.

Запуск: pytest tests/test_variant_02.py
Тут лише приклади з опису задачі; повний набір перевірок є у викладача.
"""
from conftest import load


def test_quadrants():
    M = load(2)
    result = M.stakeholder_grid([
        {"name": "Клієнт", "power": 3, "interest": 5},
        {"name": "Інспектор", "power": 5, "interest": 2},
        {"name": "Гість", "power": 1, "interest": 5},
        {"name": "Постачальник", "power": 2, "interest": 2},
    ])
    assert [(r["name"], r["quadrant"]) for r in result] == [
        ("Клієнт", "керувати уважно"), ("Інспектор", "тримати задоволеним"),
        ("Гість", "інформувати"), ("Постачальник", "спостерігати")]


def test_score_order_and_workshop():
    M = load(2)
    result = M.stakeholder_grid([{"name": "А", "power": 5, "interest": 3}, {"name": "Б", "power": 3, "interest": 3}])
    assert result == [
        {"name": "А", "quadrant": "керувати уважно", "score": 15, "order": 1, "workshop": True},
        {"name": "Б", "quadrant": "керувати уважно", "score": 9, "order": 2, "workshop": False}]


def test_duplicates_are_merged():
    M = load(2)
    result = M.stakeholder_grid([{"name": "Студент", "power": 2, "interest": 5}, {"name": "студент ", "power": 4, "interest": 3}])
    assert len(result) == 1 and result[0]["name"] == "Студент" and result[0]["score"] == 20
