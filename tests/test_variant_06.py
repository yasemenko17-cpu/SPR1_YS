"""Відкриті тести задачі 6: доступність.

Запуск: pytest tests/test_variant_06.py
Тут лише приклади з опису задачі; повний набір перевірок є у викладача.
"""
from conftest import load


def test_budget():
    f = load(6).availability
    assert f({"kind": "budget", "target": 99.9, "period": "month"}) == {"downtime_min": 43.2}
    assert f({"kind": "budget", "target": 99.99, "period": "year"}) == {"downtime_min": 52.56}


def test_chain_serial_and_replicas():
    f = load(6).availability
    assert f({"kind": "chain", "components": [{"name": "A", "availability": 99}, {"name": "B", "availability": 98}]}) == \
        {"availability": 97.02, "weakest": "B"}
    assert f({"kind": "chain", "components": [{"name": "A", "availability": 99, "replicas": 2}]}) == \
        {"availability": 99.99, "weakest": "A"}


def test_error_budget():
    result = load(6).availability({"kind": "error_budget", "target": 99.9, "period": "month", "incidents": [20, 30]})
    assert result == {"budget_min": 43.2, "spent_min": 50.0, "left_min": -6.8, "burn_pct": 115.7, "releases_allowed": False}
