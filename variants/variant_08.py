"""Задача 8. Дерево корисності: структура, ранжування, архітектурні драйвери.

Правила — у student.md (розділ 6, задача 8) та в картці вашого варіанта.
Відкриті тести: pytest tests/test_variant_08.py
"""

LEVEL = {"H": 3, "M": 2, "L": 1}


def build_utility_tree(scenarios: list[dict], max_drivers: int | None = None) -> dict:
    """Повертає {"tree", "ranking", "drivers", "deferred"}."""
    raise NotImplementedError  # TODO: реалізуйте за описом задачі
