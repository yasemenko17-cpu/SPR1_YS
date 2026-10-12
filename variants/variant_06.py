"""Задача 6. Доступність: бюджет простою, складена система, бюджет помилок.

Правила — у student.md (розділ 6, задача 6) та в картці вашого варіанта.
Відкриті тести: pytest tests/test_variant_06.py
"""

PERIOD_MINUTES = {"week": 10080, "month": 43200, "year": 525600}


def availability(spec: dict) -> dict:
    """Обчислює показники доступності за видом завдання spec["kind"]: budget, chain або error_budget."""
    raise NotImplementedError  # TODO: реалізуйте за описом задачі
