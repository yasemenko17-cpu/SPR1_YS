"""Відкриті тести задачі 8: дерево корисності.

Запуск: pytest tests/test_variant_08.py
Тут лише приклади з опису задачі; повний набір перевірок є у викладача.
"""
import pytest
from conftest import load


def U(sid, attribute, refinement, importance, difficulty):
    return {"id": sid, "attribute": attribute, "refinement": refinement, "text": "", "importance": importance,
            "difficulty": difficulty}


SCENARIOS = [
    U("Q1", "продуктивність", "затримка", "H", "M"),
    U("Q2", "доступність", "відмова", "H", "H"),
    U("Q3", "безпека", "паролі", "H", "L"),
    U("Q4", "зручність", "навчання", "L", "H"),
]


def test_ranking_drivers_deferred():
    result = load(8).build_utility_tree(SCENARIOS)
    assert result["ranking"] == ["Q2", "Q1", "Q3", "Q4"]
    assert result["drivers"] == ["Q2", "Q1"]
    assert result["deferred"] == ["Q4"]


def test_tree_shape():
    tree = load(8).build_utility_tree(SCENARIOS)["tree"]
    assert list(tree) == ["безпека", "доступність", "зручність", "продуктивність"]
    assert tree["доступність"] == {"відмова": ["Q2"]}


def test_max_drivers():
    assert load(8).build_utility_tree(SCENARIOS, max_drivers=1)["drivers"] == ["Q2"]


def test_duplicate_id():
    with pytest.raises(ValueError) as info:
        load(8).build_utility_tree([SCENARIOS[0], SCENARIOS[0]])
    assert str(info.value) == "Повторний ідентифікатор: Q1"
