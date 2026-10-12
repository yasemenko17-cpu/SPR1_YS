"""Відкриті тести задачі 7: навантаження й ємність.

Запуск: pytest tests/test_variant_07.py
Тут лише приклади з опису задачі; повний набір перевірок є у викладача.
"""
from conftest import load

SPEC = {"users": 3600, "actions_per_user_hour": 10, "peak_factor": 2, "target_utilization": 0.5, "instance_rps": 15}


def test_capacity():
    assert load(7).size_capacity(SPEC) == {"avg_rps": 10.0, "peak_rps": 20.0, "capacity_rps": 40.0,
                                           "instances": 3, "with_reserve": 3}


def test_reserve():
    assert load(7).size_capacity({**SPEC, "n_plus_one": True})["with_reserve"] == 4


def test_exact_boundary_needs_no_extra_instance():
    spec = {"users": 900, "actions_per_user_hour": 12, "peak_factor": 7, "target_utilization": 0.7, "instance_rps": 10}
    assert load(7).size_capacity(spec)["instances"] == 3


def test_latency_budget():
    spec = {**SPEC, "latency_budget": {"total_ms": 100, "components": {"a": 1, "b": 1, "c": 1}}}
    assert load(7).size_capacity(spec)["latency_ms"] == {"a": 34, "b": 33, "c": 33}
