"""Відкриті тести задачі 10: реєстр драйверів.

Запуск: pytest tests/test_variant_10.py
Тут лише приклади з опису задачі; повний набір перевірок є у викладача.
"""
import pytest
from conftest import load

TEXT = """\
goals:
  - {id: G1, priority: must}
  - {id: G2, priority: should}
scenarios:
  - {id: Q1, goal: G1}
  - {id: Q2, goal: G9}
drivers:
  - {id: D1, scenarios: [Q1, Q5]}
"""


def test_register_text():
    assert load(10).check_register_text(TEXT) == {
        "verdict": "ПОВЕРНУТО",
        "issues": ["невідома_ціль:Q2:G9", "невідомий_сценарій:D1:Q5", "ціль_без_сценаріїв:G2"],
        "coverage": {"must": {"covered": 1, "total": 1, "pct": 100.0}, "should": {"covered": 0, "total": 1, "pct": 0.0}},
        "blockers": []}


def test_clean_register():
    register = {"goals": [{"id": "G1", "priority": "must"}], "scenarios": [{"id": "Q1", "goal": "G1"}],
                "drivers": [{"id": "D1", "scenarios": ["Q1"]}]}
    assert load(10).check_register(register)["verdict"] == "ПРИЙНЯТО"


def test_missing_sections():
    with pytest.raises(ValueError) as info:
        load(10).check_register_text("goals: []\n")
    assert str(info.value) == "Реєстр має містити розділи goals, scenarios, drivers"
