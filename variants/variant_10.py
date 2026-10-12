"""Задача 10. Реєстр драйверів: перевірка цілісності та покриття цілей.

Правила — у student.md (розділ 6, задача 10) та в картці вашого варіанта.
Відкриті тести: pytest tests/test_variant_10.py
"""
import yaml

SECTIONS = ("goals", "scenarios", "drivers")
PRIORITIES = ("must", "should", "could")


def check_register_text(text: str) -> dict:
    """Читає реєстр із YAML-тексту й перевіряє його (викликає check_register)."""
    raise NotImplementedError  # TODO: реалізуйте за описом задачі


def check_register(register: dict) -> dict:
    """Повертає {"verdict", "issues", "coverage", "blockers"}."""
    raise NotImplementedError  # TODO: реалізуйте за описом задачі
