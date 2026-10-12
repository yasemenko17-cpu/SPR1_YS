"""Задача 3. Рейтинг атрибутів якості за побажаннями зацікавлених сторін.

Правила — у student.md (розділ 6, задача 3) та в картці вашого варіанта.
Відкриті тести: pytest tests/test_variant_03.py
"""


def rank_attributes(stakeholders: dict[str, int], concerns: list[dict], cover: float = 0.6) -> list[dict]:
    """Повертає список {"attribute", "weight", "share", "rank", "key"} від найвагомішого атрибута."""
    raise NotImplementedError  # TODO: реалізуйте за описом задачі
