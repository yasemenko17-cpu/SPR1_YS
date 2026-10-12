"""Задача 5. Складання сценарію якості: ідентифікатор, канонічна міра, текст у Markdown.

Правила — у student.md (розділ 6, задача 5) та в картці вашого варіанта.
Відкриті тести: pytest tests/test_variant_05.py
"""

PREFIX = {"продуктивність": "PERF", "доступність": "AVAIL", "безпека": "SEC",
          "супровідність": "MAINT", "зручність": "UX", "гнучкість": "FLEX"}


def make_scenario(spec: dict, existing_ids: list[str] | None = None) -> dict:
    """Будує сценарій: {"id", "attribute", "source", "stimulus", "environment", "artifact", "response", "measure"}."""
    raise NotImplementedError  # TODO: реалізуйте за описом задачі


def render_markdown(scenario: dict) -> str:
    """Подає сценарій у вигляді блока Markdown."""
    raise NotImplementedError  # TODO: реалізуйте за описом задачі
